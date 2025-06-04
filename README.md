# 방송대 공지사항 크롤러

방송통신대학교 공지사항을 자동으로 크롤링하고 웹 인터페이스를 통해 확인할 수 있는 애플리케이션입니다.

## 주요 기능

- 방송대 공지사항 자동 크롤링
- 공지사항 목록 조회
- 공지사항 상세 내용 확인
- 카테고리별 분류
- 모바일 반응형 UI

## 기술 스택

- Backend: Python (Flask)
- Frontend: HTML, CSS, JavaScript
- Database: MongoDB
- Crawling: Selenium

## 설치 및 실행 방법

1. 저장소 클론

```bash
git clone [repository-url]
cd knou-assignment
```

2. 실행 스크립트에 실행 권한 부여

```bash
chmod +x run.sh
```

3. 애플리케이션 실행

```bash
./run.sh
```

실행 스크립트는 다음 작업을 자동으로 수행합니다:

- Python 가상환경 생성 및 활성화
- 필요한 패키지 설치
- 환경 변수 설정
- Python 서버 실행 (http://localhost:5000)
- 프론트엔드 서버 실행 (http://localhost:8000)

웹 브라우저에서 http://localhost:8000 으로 접속하여 공지사항을 확인할 수 있습니다.

## 프로젝트 구조

```
.
├── app.py              # Flask 서버 메인 파일
├── knou_crawler.py     # 크롤러 구현
├── notice_summarizer.py # 공지사항 요약 처리
├── db_manager.py       # 데이터베이스 관리
├── frontend/          # 프론트엔드 파일
│   ├── index.html     # 메인 페이지
│   ├── styles.css     # 스타일시트
│   └── app.js         # 프론트엔드 로직
├── requirements.txt   # Python 패키지 의존성
└── run.sh            # 실행 스크립트
```

## API 엔드포인트

- `GET /notices`: 공지사항 목록 조회
- `GET /notices/<id>`: 특정 공지사항 상세 내용 조회

## 개발 환경 설정

1. MongoDB 설치 및 실행
2. Python 3.8 이상 설치
3. Chrome 브라우저 설치 (크롤링용)

## 라이선스

MIT License
