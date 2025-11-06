"""
토픽 모델링 및 t-SNE 시각화
"""
import re
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.manifold import TSNE
from typing import List, Dict, Tuple
import json

def preprocess_text(text: str) -> str:
    """텍스트 전처리"""
    # 특수문자 제거 (한글, 영문, 숫자, 공백만 남김)
    text = re.sub(r'[^가-힣a-zA-Z0-9\s]', ' ', text)
    # 여러 공백을 하나로
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def perform_topic_modeling(
    reviews: List[str], 
    n_topics: int = 5,
    n_top_words: int = 10,
    max_features: int = 1000
) -> Dict:
    """
    LDA 토픽 모델링 수행
    
    Args:
        reviews: 리뷰 텍스트 리스트
        n_topics: 추출할 토픽 개수
        n_top_words: 토픽당 상위 단어 개수
        max_features: 최대 특성 개수
        
    Returns:
        토픽 모델링 결과 딕셔너리
    """
    
    if len(reviews) < 3:
        raise ValueError("토픽 모델링을 수행하려면 최소 3개 이상의 리뷰가 필요합니다.")
    
    # 텍스트 전처리
    processed_reviews = [preprocess_text(review) for review in reviews]
    
    # CountVectorizer로 문서-단어 행렬 생성
    vectorizer = CountVectorizer(
        max_features=max_features,
        min_df=2,  # 최소 2개 문서에 등장
        max_df=0.8,  # 최대 80% 문서에 등장
        ngram_range=(1, 2)  # 1-gram과 2-gram
    )
    
    try:
        doc_term_matrix = vectorizer.fit_transform(processed_reviews)
    except ValueError as e:
        raise ValueError("리뷰 데이터가 충분하지 않거나 적절한 단어를 추출할 수 없습니다.")
    
    # 실제 토픽 개수 조정 (리뷰 수보다 적게)
    actual_n_topics = min(n_topics, len(reviews) - 1, doc_term_matrix.shape[1])
    if actual_n_topics < 2:
        actual_n_topics = 2
    
    # LDA 모델 학습
    lda_model = LatentDirichletAllocation(
        n_components=actual_n_topics,
        random_state=42,
        max_iter=20,
        learning_method='batch'
    )
    
    doc_topic_dist = lda_model.fit_transform(doc_term_matrix)
    
    # 각 토픽의 상위 단어 추출
    feature_names = vectorizer.get_feature_names_out()
    topics = []
    
    for topic_idx, topic in enumerate(lda_model.components_):
        top_indices = topic.argsort()[-n_top_words:][::-1]
        top_words = [feature_names[i] for i in top_indices]
        top_weights = [float(topic[i]) for i in top_indices]
        
        topics.append({
            'topic_id': topic_idx,
            'words': top_words,
            'weights': top_weights
        })
    
    # t-SNE로 차원 축소 (2D)
    if len(reviews) >= 3:
        try:
            # perplexity는 샘플 수보다 작아야 함
            perplexity = min(30, len(reviews) - 1)
            if perplexity < 2:
                perplexity = 2
                
            tsne = TSNE(
                n_components=2,
                random_state=42,
                perplexity=perplexity,
                n_iter=300
            )
            tsne_results = tsne.fit_transform(doc_topic_dist)
            
            # 각 문서의 주요 토픽 결정
            dominant_topics = doc_topic_dist.argmax(axis=1)
            
            # t-SNE 결과 준비
            tsne_data = []
            for i, (x, y) in enumerate(tsne_results):
                tsne_data.append({
                    'x': float(x),
                    'y': float(y),
                    'topic': int(dominant_topics[i]),
                    'review_index': i,
                    'review_snippet': reviews[i][:100] + '...' if len(reviews[i]) > 100 else reviews[i]
                })
        except Exception as e:
            print(f"t-SNE 오류: {e}")
            # t-SNE 실패 시 기본값
            tsne_data = []
            for i in range(len(reviews)):
                tsne_data.append({
                    'x': float(i),
                    'y': 0.0,
                    'topic': int(doc_topic_dist[i].argmax()),
                    'review_index': i,
                    'review_snippet': reviews[i][:100] + '...' if len(reviews[i]) > 100 else reviews[i]
                })
    else:
        tsne_data = []
    
    return {
        'n_topics': actual_n_topics,
        'topics': topics,
        'tsne_data': tsne_data,
        'n_reviews': len(reviews)
    }


def analyze_reviews_topic_modeling(reviews_data: List[Dict]) -> Dict:
    """
    리뷰 데이터에 대해 토픽 모델링 수행
    
    Args:
        reviews_data: 리뷰 딕셔너리 리스트 (review_content 키 필요)
        
    Returns:
        토픽 모델링 결과
    """
    # 리뷰 텍스트 추출
    reviews = [r.get('review_content', '') for r in reviews_data if r.get('review_content')]
    
    if len(reviews) < 3:
        raise ValueError(f"토픽 모델링을 수행하려면 최소 3개 이상의 리뷰가 필요합니다. (현재: {len(reviews)}개)")
    
    # 토픽 개수는 리뷰 수에 따라 조정
    n_topics = min(5, max(2, len(reviews) // 3))
    
    result = perform_topic_modeling(reviews, n_topics=n_topics)
    
    return result





