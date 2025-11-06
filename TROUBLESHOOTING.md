# 🔧 문제 해결 가이드

## "[Errno 2] No such file or directory" 또는 "UnicodeDecodeError" 오류

이 오류는 필요한 파일이 없거나 잘못된 인코딩으로 저장되었을 때 발생합니다.

### 빠른 해결 방법

**`fix_and_restart.bat` 파일을 실행하세요!**

이 파일이 자동으로 다음을 수행합니다:
1. ✅ 기존 서버 종료
2. ✅ `.env` 환경 설정 파일 생성
3. ✅ 데이터베이스 확인
4. ✅ 서버 재시작

```bash
fix_and_restart.bat
```

### 수동 해결 방법

#### 1단계: .env 파일 생성

PowerShell에서 다음 명령어를 실행하세요 (UTF-8 인코딩 문제 방지):

```powershell
cd backend
[System.IO.File]::WriteAllText(".env", "GEMINI_API_KEY=AIzaSyD59CF1brDrcU_QhAMhcPkoj4PDhEuKmRg`n", [System.Text.Encoding]::UTF8)
cd ..
```

또는 수동으로 `backend\.env` 파일을 만들고 다음 내용을 추가하세요:

```env
GEMINI_API_KEY=AIzaSyD59CF1brDrcU_QhAMhcPkoj4PDhEuKmRg
```

⚠️ **중요**: 파일을 **UTF-8 인코딩**으로 저장해야 합니다!

#### 2단계: 서버 재시작

```bash
stop_all.bat
start_all.bat
```

---

## 기타 일반적인 문제

### 포트 충돌 오류

**증상**: "Address already in use" 또는 포트를 사용할 수 없다는 오류

**해결방법**:
```bash
stop_all.bat
```

### 패키지 설치 오류

**증상**: 모듈을 찾을 수 없다는 오류

**해결방법**:
```bash
install_dependencies.bat
```

### Playwright 브라우저 오류

**증상**: "Executable doesn't exist" 오류

**해결방법**:
```bash
cd backend
python -m playwright install chromium
cd ..
```

### 데이터베이스 초기화

**증상**: 데이터베이스 스키마 오류

**해결방법**:
```bash
# 데이터베이스 파일 삭제
del backend\app_review.db

# 서버 재시작 (자동으로 재생성됨)
start_all.bat
```

### Frontend 빌드 오류

**증상**: Vite 빌드 실패

**해결방법**:
```bash
cd frontend
del /s /q node_modules
npm install
cd ..
```

---

## 로그 확인 방법

### Backend 로그
Backend 서버 창에서 로그를 확인할 수 있습니다.

### Frontend 로그
Frontend 서버 창에서 로그를 확인할 수 있습니다.

### 브라우저 콘솔
1. 브라우저에서 F12 키를 누릅니다
2. Console 탭을 확인합니다
3. Network 탭에서 API 요청 상태를 확인합니다

---

## 완전 초기화

모든 것을 처음부터 다시 설정하려면:

```bash
# 1. 서버 종료
stop_all.bat

# 2. 데이터베이스 삭제 (선택사항)
del backend\app_review.db

# 3. 의존성 재설치
install_dependencies.bat

# 4. 서버 시작
start_all.bat
```

---

## 여전히 문제가 있나요?

다음 정보를 확인하세요:

1. **Python 버전**: Python 3.10 이상 필요
   ```bash
   python --version
   ```

2. **Node.js 버전**: Node.js 16 이상 필요
   ```bash
   node --version
   ```

3. **네트워크 연결**: 인터넷 연결 확인

4. **방화벽**: 포트 8000, 3000 허용 확인

5. **디스크 공간**: 최소 1GB 이상 여유 공간 필요

