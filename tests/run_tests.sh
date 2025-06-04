#!/bin/bash

# 색상 정의
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 가상환경 활성화
source ../venv/bin/activate

# 필요한 패키지 설치
echo -e "${YELLOW}필요한 패키지를 설치합니다...${NC}"
uv pip install -r ../requirements.txt

# 프로젝트 루트 디렉토리를 PYTHONPATH에 추가
export PYTHONPATH="${PYTHONPATH}:$(cd .. && pwd)"

echo -e "${YELLOW}테스트를 실행합니다...${NC}"

# 테스트 실행
python3 -m unittest discover -s tests -p "test_*.py"

# 테스트 결과 확인
if [ $? -eq 0 ]; then
    echo -e "${GREEN}모든 테스트가 성공적으로 완료되었습니다.${NC}"
else
    echo -e "${RED}테스트 실행 중 오류가 발생했습니다.${NC}"
    exit 1
fi 