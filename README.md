# Prime Notice - 방송통신대학교 공지사항 자동 요약 시스템

## 프로젝트 개요

방송통신대학교 학생들을 위한 공지사항 자동 수집 및 요약 시스템입니다. AI 기술을 활용하여 다양한 채널의 공지사항을 수집하고, 중요 내용을 요약하여 제공합니다.

## 주요 기능

- 웹 크롤링을 통한 공지사항 자동 수집
- AI 기반 텍스트 분석 및 요약
- 사용자 맞춤형 알림 시스템
- 다양한 플랫폼 지원 (웹, 모바일)

## 기술 스택

- Backend: Python (Flask)
- Frontend: React.js
- Database: MongoDB
- AI/NLP: OpenAI API, NLTK, spaCy
- Web Crawling: BeautifulSoup, Selenium

## 설치 방법

1. 저장소 클론

```bash
git clone [repository-url]
```

2. 가상환경 생성 및 활성화

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. 의존성 설치

```bash
pip install -r requirements.txt
```

4. 환경 변수 설정
   `.env` 파일을 생성하고 필요한 API 키 등을 설정합니다.

## 실행 방법

```bash
python app.py
```

## 프로젝트 구조

```
prime-notice/
├── app/
│   ├── __init__.py
│   ├── crawler/
│   ├── nlp/
│   ├── models/
│   └── utils/
├── frontend/
├── tests/
├── requirements.txt
└── README.md
```

## 라이선스

MIT License
