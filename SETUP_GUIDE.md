# 🚀 빠른 시작 가이드

## Windows 사용자 (배치 파일 사용 - 권장)

### 1단계: 의존성 설치

프로젝트 루트 폴더에서 `install_dependencies.bat` 파일을 더블클릭하거나 실행:

```powershell
install_dependencies.bat
```

이 파일이 자동으로 다음을 수행합니다:
- Backend Python 패키지 설치
- Playwright 브라우저 설치
- Frontend npm 패키지 설치

### 2단계: 서버 시작

`start_all.bat` 파일을 더블클릭하거나 실행:

```powershell
start_all.bat
```

이 파일이 Backend와 Frontend 서버를 별도 창에서 자동으로 시작합니다.

### 3단계: 브라우저에서 접속

브라우저에서 http://localhost:3000 으로 접속

### 서버 종료

`stop_all.bat` 파일을 실행하여 모든 서버를 한 번에 종료:

```powershell
stop_all.bat
```

---

## Windows 사용자 (수동 설치)

### 1단계: Python 패키지 설치

```powershell
cd backend
pip install -r requirements.txt
playwright install chromium
```

### 2단계: 환경 변수 설정

`backend/.env.example` 파일 내용을 `backend/.env`로 복사 (이미 설정됨)

### 3단계: Backend 실행

```powershell
cd backend
python main.py
```

또는 배치 파일 실행:
```powershell
.\start_backend.bat
```

### 4단계: Frontend 설치 및 실행 (새 터미널)

```powershell
cd frontend
npm install
npm run dev
```

또는 배치 파일 실행:
```powershell
.\start_frontend.bat
```

## 브라우저에서 열기

앱이 실행되면 브라우저에서 다음 주소로 접속하세요:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API 문서: http://localhost:8000/docs

## 예제 앱 ID

테스트해볼 수 있는 Google Play Store 앱 ID:

- `com.kakao.talk` - 카카오톡
- `com.nhn.android.search` - 네이버
- `com.kakaobank.channel` - 카카오뱅크
- `com.skt.skaf.A000Z00040` - 원스토어
- `com.nhn.android.webtoon` - 네이버 웹툰

## 문제 해결

### Playwright 오류
```powershell
playwright install --force chromium
```

### 포트 충돌
Backend(8000)나 Frontend(3000) 포트가 이미 사용 중이라면:
- 해당 포트를 사용하는 프로그램을 종료하거나
- `backend/main.py`와 `frontend/vite.config.js`에서 포트 변경

### 데이터베이스 연결 오류
- Supabase 연결 정보가 올바른지 확인
- 인터넷 연결 확인

## 사용 팁

1. **크롤링 시간**: 앱 정보와 리뷰 수집에 5-10초 정도 소요됩니다
2. **AI 분석**: 리뷰 10개 분석에 약 30초-1분 소요됩니다
3. **리뷰 수**: 기본적으로 최신 리뷰 10개를 수집합니다
4. **재수집**: 같은 앱을 다시 수집하려면 먼저 삭제 버튼으로 삭제하세요

