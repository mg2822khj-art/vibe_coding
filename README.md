# 📱 앱 리뷰 분석기

Google Play Store의 앱 리뷰를 자동으로 수집하고 Gemini AI로 분석하는 웹 애플리케이션입니다.

## 🎯 주요 기능

1. **앱 정보 수집**
   - Google Play Store에서 앱 정보 크롤링
   - 앱명, 리뷰수, 다운로드수, 별점 자동 수집

2. **리뷰 수집**
   - 최대 10개의 최신 리뷰 수집
   - 별점, 리뷰 내용, 작성일 정보 저장

3. **AI 분석**
   - Gemini AI를 활용한 전체 리뷰 분석
   - 개별 리뷰 감정 분석 및 요약
   - 주요 피드백 및 개선 제안사항 도출

4. **토픽 모델링**
   - LDA 알고리즘을 통한 토픽 추출
   - t-SNE를 통한 2차원 시각화

5. **데이터 관리**
   - PostgreSQL(Supabase) 데이터베이스에 저장
   - 수집된 데이터 조회 및 삭제

## 🛠️ 기술 스택

### Backend
- **FastAPI**: Python 웹 프레임워크
- **Playwright**: 웹 크롤링
- **SQLAlchemy**: ORM
- **PostgreSQL**: 데이터베이스 (Supabase)
- **Google Gemini AI**: 리뷰 분석
- **scikit-learn**: LDA 토픽 모델링, t-SNE 시각화

### Frontend
- **Vite**: 빌드 도구
- **React**: UI 라이브러리
- **Axios**: HTTP 클라이언트
- **Chart.js**: 데이터 시각화

## 📦 설치 방법

### 1. 저장소 클론
```bash
git clone https://github.com/mg2822khj-art/vibe_coding.git
cd vibe_coding
```

### 2. Backend 설정

```bash
cd backend

# 패키지 설치
pip install -r requirements.txt

# Playwright 브라우저 설치
playwright install chromium
```

### 3. 환경 변수 설정

`backend/.env` 파일을 생성하세요:

```bash
DATABASE_URL=your_supabase_database_url
GEMINI_API_KEY=your_gemini_api_key
```

### 4. Frontend 설정

```bash
cd frontend

# 패키지 설치
npm install
```

## 🚀 실행 방법

### Backend 실행
```bash
cd backend
python main.py
```
서버가 `http://localhost:8000`에서 실행됩니다.

### Frontend 실행
새 터미널에서:
```bash
cd frontend
npm run dev
```
프론트엔드가 `http://localhost:3000`에서 실행됩니다.

## 📖 사용 방법

1. **앱 ID 입력**: Google Play Store의 앱 패키지 ID를 입력합니다
   - 예: `com.kakao.talk`, `com.nhn.android.search`
   
2. **리뷰 수집**: "리뷰 수집" 버튼을 클릭하여 앱 정보와 리뷰를 크롤링합니다

3. **AI 분석**: "앱 리뷰 분석" 버튼을 클릭하여 Gemini AI로 리뷰를 분석합니다

4. **토픽 모델링**: "토픽 모델링" 버튼을 클릭하여 토픽 추출 및 t-SNE 시각화를 확인합니다

## 🔍 API 엔드포인트

- `POST /api/apps/crawl` - 앱 정보 및 리뷰 크롤링
- `GET /api/apps` - 모든 앱 목록 조회
- `GET /api/apps/{app_id}` - 특정 앱 상세 정보 조회
- `POST /api/apps/analyze` - 리뷰 AI 분석
- `POST /api/apps/topic-modeling` - 토픽 모델링 및 t-SNE 시각화
- `DELETE /api/apps/{app_id}` - 앱 정보 삭제

## 📊 데이터베이스 구조

### app_info 테이블
- id (PK)
- app_id (UNIQUE)
- app_name
- review_count
- download_count
- rating
- overall_analysis
- created_at

### app_review 테이블
- id (PK)
- app_id (FK)
- rating
- review_content
- review_date
- individual_analysis
- created_at

## ⚠️ 주의사항

1. **크롤링 제한**: Google Play Store의 구조 변경 시 셀렉터 수정이 필요할 수 있습니다
2. **API 제한**: Gemini API의 사용량 제한에 유의하세요
3. **네트워크**: 안정적인 인터넷 연결이 필요합니다
4. **브라우저**: Playwright는 Chromium 브라우저를 사용합니다

## 🔧 문제 해결

### Playwright 설치 오류
```bash
playwright install --force chromium
```

### 데이터베이스 연결 오류
- `.env` 파일의 `DATABASE_URL`이 올바른지 확인하세요
- Supabase 프로젝트가 활성화되어 있는지 확인하세요

### CORS 오류
- Backend가 8000 포트에서 실행 중인지 확인하세요
- Frontend가 3000 포트에서 실행 중인지 확인하세요

## 📝 라이센스

이 프로젝트는 개인 학습 및 연구 목적으로 제작되었습니다.

## 🤝 기여

버그 리포트나 기능 제안은 환영합니다!
