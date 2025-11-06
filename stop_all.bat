@echo off
chcp 65001 > nul
echo ====================================
echo 서버 종료 중...
echo ====================================
echo.

echo Backend 서버 종료 중...
for /f "tokens=5" %%a in ('netstat -aon ^| find ":8000" ^| find "LISTENING"') do (
    taskkill /F /PID %%a > nul 2>&1
    if not errorlevel 1 (
        echo ✓ Backend 서버가 종료되었습니다 (포트 8000)
    )
)

echo Frontend 서버 종료 중...
for /f "tokens=5" %%a in ('netstat -aon ^| find ":3000" ^| find "LISTENING"') do (
    taskkill /F /PID %%a > nul 2>&1
    if not errorlevel 1 (
        echo ✓ Frontend 서버가 종료되었습니다 (포트 3000)
    )
)

echo.
echo Node.js 프로세스 정리 중...
taskkill /F /IM node.exe > nul 2>&1
taskkill /F /IM python.exe > nul 2>&1

echo.
echo ====================================
echo 모든 서버가 종료되었습니다.
echo ====================================
echo.
pause






