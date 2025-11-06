@echo off
chcp 65001 > nul
echo ====================================
echo 의존성 패키지 설치
echo ====================================
echo.

echo [0/4] 환경 설정 파일 생성 중...
if not exist "backend\.env" (
    powershell -Command "[System.IO.File]::WriteAllText('backend\.env', 'GEMINI_API_KEY=AIzaSyD59CF1brDrcU_QhAMhcPkoj4PDhEuKmRg`n', [System.Text.Encoding]::UTF8)"
    echo ✓ .env 파일이 생성되었습니다
) else (
    echo ✓ .env 파일이 이미 존재합니다
)
echo.

echo [1/4] Backend 패키지 설치 중...
cd backend
echo Python 버전:
python --version
echo.
echo pip로 패키지를 설치합니다...
python -m pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Backend 패키지 설치 실패
    cd ..
    pause
    exit /b 1
)
echo ✓ Backend 패키지 설치 완료
echo.

echo [2/4] Playwright 브라우저 설치 중...
python -m playwright install chromium
if errorlevel 1 (
    echo ❌ Playwright 브라우저 설치 실패
    cd ..
    pause
    exit /b 1
)
echo ✓ Playwright 브라우저 설치 완료
cd ..
echo.

echo [3/4] Frontend 패키지 설치 중...
cd frontend
echo Node.js 버전:
node --version
echo npm 버전:
npm --version
echo.
echo npm으로 패키지를 설치합니다...
npm install
if errorlevel 1 (
    echo ❌ Frontend 패키지 설치 실패
    cd ..
    pause
    exit /b 1
)
echo ✓ Frontend 패키지 설치 완료
cd ..
echo.

echo [4/4] 데이터베이스 초기화 중...
if not exist "backend\app_review.db" (
    echo ✓ 처음 실행 시 자동으로 생성됩니다
) else (
    echo ✓ 데이터베이스 파일이 이미 존재합니다
)
echo.

echo ====================================
echo 모든 의존성 설치 완료!
echo ====================================
echo.
echo 이제 start_all.bat 파일을 실행하여
echo 서버를 시작할 수 있습니다.
echo.
pause

