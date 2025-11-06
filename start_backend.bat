@echo off
chcp 65001 > nul
echo ====================================
echo Backend 서버 시작
echo ====================================
echo.

cd backend

echo Python 버전 확인...
python --version
echo.

echo Backend 서버를 시작합니다...
echo 서버 주소: http://localhost:8000
echo API 문서: http://localhost:8000/docs
echo.
echo 서버를 종료하려면 Ctrl+C를 누르세요.
echo.

python main.py

pause






