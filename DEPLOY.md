# Prime Notice 배포 가이드

## 필수 요구사항

- Python 3.13+
- MongoDB 6.0+
- Node.js 18+ (프론트엔드 빌드용)

## 배포 단계

### 1. 환경 설정

```bash
# 저장소 클론
git clone [repository_url]
cd prime-notice

# 가상환경 생성 및 활성화
python3 -m venv venv
source venv/bin/activate

# 의존성 설치
pip install -r requirements.txt

# 환경 변수 설정
cp .env.example .env
# .env 파일을 편집하여 실제 값 입력
```

### 2. MongoDB 설정

```bash
# MongoDB 설치 (Ubuntu/Debian)
sudo apt-get install mongodb

# MongoDB 서비스 시작
sudo systemctl start mongodb
sudo systemctl enable mongodb
```

### 3. 서버 실행

```bash
# 실행 권한 부여
chmod +x run.sh

# 서버 시작
./run.sh
```

### 4. 프론트엔드 배포

```bash
cd frontend
npm install
npm run build
```

## 모니터링

- 로그 파일: `logs/access.log`, `logs/error.log`
- MongoDB 상태: `mongosh --eval "db.serverStatus()"`

## 문제 해결

1. MongoDB 연결 오류

   - MongoDB 서비스 상태 확인
   - 연결 문자열 확인

2. 서버 시작 실패

   - 포트 사용 중 여부 확인
   - 환경 변수 설정 확인

3. 프론트엔드 로드 실패
   - API 엔드포인트 연결 확인
   - CORS 설정 확인

## 백업 및 복구

```bash
# MongoDB 백업
mongodump --db prime_notice --out /backup/$(date +%Y%m%d)

# MongoDB 복구
mongorestore --db prime_notice /backup/[backup_date]
```
