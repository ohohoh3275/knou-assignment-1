#!/bin/bash

# 가상환경이 없으면 생성
if [ ! -d "venv" ]; then
    echo "가상환경을 생성합니다..."
    python3 -m venv venv
fi

# 가상환경 활성화
source venv/bin/activate

# requirements.txt가 있으면 패키지 설치
if [ -f "requirements.txt" ]; then
    echo "필요한 패키지를 설치합니다..."
    pip3 install -r requirements.txt
fi

# .env 파일이 없으면 .env.example을 복사
if [ ! -f ".env" ] && [ -f ".env.example" ]; then
    echo "환경 변수 파일을 설정합니다..."
    cp .env.example .env
fi

# Python 서버 실행 (백그라운드)
echo "Python 서버를 시작합니다..."
python3 app.py &
PYTHON_PID=$!

# 프론트엔드 서버 실행 (간단한 HTTP 서버 사용)
echo "프론트엔드 서버를 시작합니다..."
cd frontend
python3 -m http.server 8000 &
FRONTEND_PID=$!

# 프로세스 종료 함수
cleanup() {
    echo "서버를 종료합니다..."
    kill $PYTHON_PID
    kill $FRONTEND_PID
    exit 0
}

# SIGINT (Ctrl+C) 시그널 핸들러 등록
trap cleanup SIGINT

echo "서버가 시작되었습니다."
echo "Python 서버: http://localhost:5000"
echo "프론트엔드: http://localhost:8000"
echo "종료하려면 Ctrl+C를 누르세요."

# 프로세스가 종료될 때까지 대기
wait 