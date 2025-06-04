#!/bin/bash

# 가상환경 활성화
source venv/bin/activate

# 환경 변수 로드
if [ -f .env ]; then
    export $(cat .env | xargs)
else
    echo "Error: .env file not found"
    exit 1
fi

# MongoDB 상태 확인
if ! mongosh --eval "db.version()" > /dev/null 2>&1; then
    echo "Error: MongoDB is not running"
    exit 1
fi

# 필요한 디렉토리 생성
mkdir -p logs

# 서버 실행
echo "Starting Prime Notice server..."
gunicorn --bind $HOST:$PORT \
         --workers 4 \
         --access-logfile logs/access.log \
         --error-logfile logs/error.log \
         --capture-output \
         app:app 