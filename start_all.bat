@echo off
chcp 65001 > nul
echo ====================================
echo 앱 리뷰 분석기 서버 시작
echo ====================================
echo.

echo [1/2] Backend 서버 시작 중...
cd backend
start "Backend Server" cmd /k "python main.py"
cd ..
echo ✓ Backend 서버가 시작되었습니다 (http://localhost:8000)
echo.

timeout /t 3 /nobreak > nul

echo [2/2] Frontend 서버 시작 중...
cd frontend
start "Frontend Server" cmd /k "npm run dev"
cd ..
echo ✓ Frontend 서버가 시작되었습니다 (http://localhost:3000)
echo.

echo ====================================
echo 모든 서버가 시작되었습니다!
echo ====================================
echo.
echo 브라우저에서 다음 주소로 접속하세요:
echo 👉 http://localhost:3000
echo.
echo Backend API 문서:
echo 👉 http://localhost:8000/docs
echo.
echo 서버를 종료하려면 각 창을 닫거나
echo stop_all.bat 파일을 실행하세요.
echo.
pause






