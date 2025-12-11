# 충청북도 우수모범업소 조회 웹 애플리케이션

공공데이터포털의 충청북도 우수모범업소 평가결과 API를 사용하여 음식점 정보를 조회하는 웹 애플리케이션입니다.

## 실행 방법

### 방법 1: Python 로컬 서버 사용 (권장)

1. Python 3가 설치되어 있는지 확인하세요.
2. 터미널/명령 프롬프트에서 다음 명령을 실행하세요:

```bash
python server.py
```

또는 Windows에서:

```bash
server.bat
```

3. 브라우저에서 `http://localhost:8000` 으로 접속하세요.

### 방법 2: Node.js http-server 사용

1. Node.js가 설치되어 있다면:

```bash
npx http-server -p 8000 --cors
```

2. 브라우저에서 `http://localhost:8000` 으로 접속하세요.

### 방법 3: 다른 로컬 서버 사용

- VS Code의 Live Server 확장 프로그램 사용
- 또는 다른 로컬 서버 도구 사용

## 중요 사항

⚠️ **CORS 오류 해결**: 공공데이터포털 API는 브라우저에서 직접 호출 시 CORS 정책으로 인해 차단될 수 있습니다. 반드시 로컬 서버를 통해 실행해야 합니다.

## 파일 구조

- `index.html` - 메인 HTML 파일 (HTML, CSS, JavaScript 포함)
- `server.py` - Python 로컬 서버 스크립트
- `server.bat` - Windows용 서버 실행 배치 파일
- `음식점api.txt` - API 문서

## 기능

- 충청북도 우수모범업소 10개 조회
- 업소명, 위치, 전화번호, 메뉴 등 정보 표시
- 반응형 그리드 레이아웃
- 모던한 UI 디자인

