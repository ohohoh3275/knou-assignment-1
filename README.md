# 공지사항 크롤러

이 프로젝트는 학교의 공지사항을 크롤링하여 웹 인터페이스로 보여주는 애플리케이션입니다.

## 기능

- 공지사항 자동 크롤링
- 웹 인터페이스를 통한 공지사항 조회
- MongoDB를 사용한 데이터 저장
- 자동화된 테스트

## 설치 및 실행

### 1. MongoDB 설치 (brew)

```bash
# Homebrew를 통한 MongoDB 설치
brew tap mongodb/brew
brew install mongodb-community
```

### 2. uv 설치

- uv install (https://docs.astral.sh/uv/getting-started/installation)

```
uv init
```


## 개발 환경 설정

1. Python 3.8 이상 설치
2. MongoDB 설치
3. ./run.sh (chmod +x run.sh)
