#!/bin/bash

# 색상 정의
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# # MongoDB 설치 확인
# check_mongodb_installation() {
#     if ! command -v mongosh &> /dev/null; then
#         echo -e "${RED}MongoDB가 설치되어 있지 않습니다.${NC}"
#         echo -e "${YELLOW}다음 명령어로 MongoDB를 설치해주세요:${NC}"
#         echo "brew tap mongodb/brew"
#         echo "brew install mongodb-community"
#         exit 1
#     fi
# }

# # MongoDB 상태 확인 및 시작
# check_mongodb() {
#     echo -e "${YELLOW}MongoDB 상태를 확인합니다...${NC}"
    
#     # MongoDB 서비스 상태 확인
#     if ! brew services list | grep -q "mongodb-community.*started"; then
#         echo -e "${YELLOW}MongoDB를 시작합니다...${NC}"
#         brew services start mongodb-community
        
#         # MongoDB 시작 대기
#         echo -e "${YELLOW}MongoDB 시작을 기다립니다...${NC}"
#         sleep 5
        
#         # MongoDB 연결 테스트
#         if ! mongosh --eval "db.version()" > /dev/null 2>&1; then
#             echo -e "${RED}MongoDB 시작에 실패했습니다.${NC}"
#             echo -e "${YELLOW}MongoDB가 설치되어 있는지 확인해주세요:${NC}"
#             echo "brew tap mongodb/brew"
#             echo "brew install mongodb-community"
#             exit 1
#         fi
#     fi
    
#     echo -e "${GREEN}MongoDB가 실행 중입니다.${NC}"
# }

# 데이터베이스 초기화
init_database() {
    
    # 데이터베이스 초기화 스크립트 실행
    python3 app/db/init_db.py
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}데이터베이스 초기화가 완료되었습니다.${NC}"
    else
        echo -e "${RED}데이터베이스 초기화에 실패했습니다.${NC}"
        exit 1
    fi
}

init_database
