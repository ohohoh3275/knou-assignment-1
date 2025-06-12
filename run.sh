#!/bin/bash

# 색상 정의
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# # MongoDB 시작 스크립트 실행
# echo -e "${YELLOW}MongoDB를 시작합니다...${NC}"
# ./scripts/start_mongodb.sh
# if [ $? -ne 0 ]; then
#     echo -e "${RED}MongoDB 시작에 실패했습니다.${NC}"
#     exit 1
# fi

# # 가상환경이 없으면 생성
if [ ! -d ".venv" ]; then
    echo -e "${YELLOW}기존 venv 삭제...${NC}"
    uv venv --python 3.8
else
    echo -e "${YELLOW}가상환경을 생성합니다...${NC}"
    python3 -m venv venv
fi

# # 가상환경 활성화
source .venv/bin/activate

# uv 패키지 설치
echo -e "${YELLOW}필요한 패키지를 설치합니다...${NC}"
uv pip install -r <(uv pip compile pyproject.toml)

# playwright install
echo -e "${YELLOW}playwright 패키지를 설치합니다...${NC}"
python3 -m playwright install


# # .env 파일이 없으면 .env.example을 복사
# if [ ! -f ".env" ] && [ -f ".env.example" ]; then
#     echo -e "${YELLOW}환경 변수 파일을 설정합니다...${NC}"
#     cp .env.example .env
# fi

# database connected -테스트 실행
echo -e "${YELLOW} Database connected 테스트를 실행합니다...${NC}"
python3 -m unittest tests.test_mongodb_connected

# # 테스트 실패 시 종료
# if [ $TEST_RESULT -ne 0 ]; then
#     echo -e "${RED}테스트가 실패했습니다. 앱을 실행할 수 없습니다.${NC}"
#     exit 1
# fi

# echo -e "${GREEN}테스트가 성공적으로 완료되었습니다.${NC}"



# Python 서버 실행 (백그라운드)
echo -e "${YELLOW}Python 서버를 시작합니다...${NC}"
uv run app.py &
PYTHON_PID=$!

# 프론트엔드 서버 실행 (간단한 HTTP 서버 사용)
echo -e "${YELLOW}프론트엔드 서버를 시작합니다...${NC}"
cd frontend
python -m http.server 5000 &
FRONTEND_PID=$!

# 프로세스 종료 함수
cleanup() {
    echo -e "${YELLOW}서버를 종료합니다...${NC}"
    kill $PYTHON_PID
    kill $FRONTEND_PID
    exit 0
}

# SIGINT (Ctrl+C) 시그널 핸들러 등록
trap cleanup SIGINT

echo -e "${GREEN}서버가 시작되었습니다.${NC}"
echo -e "${GREEN}Python 서버: http://localhost:8000${NC}"
echo -e "${GREEN}프론트엔드: http://localhost:5000${NC}"
echo -e "${YELLOW}종료하려면 Ctrl+C를 누르세요.${NC}"

# 프로세스가 종료될 때까지 대기
wait 