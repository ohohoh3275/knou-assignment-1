# 방송대 공지사항 크롤러

이 프로젝트는 한국방송통신대학교의 공지사항을 크롤링하여 웹 인터페이스로 보여주는 애플리케이션입니다.

## 기능

- 방송대 공지사항 자동 크롤링
- 웹 인터페이스를 통한 공지사항 조회
- MongoDB를 사용한 데이터 저장
- 자동화된 테스트

## 설치 및 실행

### 1. MongoDB 설치 (macOS)

```bash
# Homebrew를 통한 MongoDB 설치
brew tap mongodb/brew
brew install mongodb-community
```

### 2. 프로젝트 실행

```bash
# 실행 권한 부여
chmod +x run.sh
chmod +x scripts/start_mongodb.sh

# 실행
./run.sh
```

실행 스크립트는 다음 작업을 자동으로 수행합니다:

1. MongoDB 상태 확인 및 시작
2. Python 가상환경 설정
3. 필요한 패키지 설치
4. 환경 변수 설정
5. 테스트 실행
6. 서버 시작

## 프로젝트 구조

```
.
├── app/
│   ├── crawler/
│   │   └── notice_crawler.py
│   ├── db/
│   │   └── db_manager.py
│   └── app.py
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── app.js
├── tests/
│   ├── test_db_manager.py
│   └── run_tests.sh
├── scripts/
│   └── start_mongodb.sh
├── requirements.txt
├── .env.example
└── run.sh
```

## 테스트

프로젝트에는 자동화된 테스트가 포함되어 있습니다:

- 데이터베이스 연결 테스트
- 공지사항 중복 처리 테스트
- 최근 공지사항 조회 테스트

테스트는 애플리케이션 시작 전에 자동으로 실행되며, 테스트가 실패하면 애플리케이션이 실행되지 않습니다.

## 개발 환경 설정

1. Python 3.8 이상 설치
2. MongoDB 설치
3. 가상환경 생성 및 활성화:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. 필요한 패키지 설치:
   ```bash
   pip3 install -r requirements.txt
   ```
5. 환경 변수 설정:
   ```bash
   cp .env.example .env
   ```

## MongoDB 관리

MongoDB는 `scripts/start_mongodb.sh` 스크립트를 통해 관리됩니다:

- MongoDB 서비스 상태 확인
- 필요한 경우 자동 시작
- 연결 테스트

수동으로 MongoDB를 시작하려면:

```bash
./scripts/start_mongodb.sh
```

## 라이선스

MIT License
