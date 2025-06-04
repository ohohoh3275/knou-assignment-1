from models import db_manager

def init_database():
    """데이터베이스 초기화 함수"""
    try:
        db_manager.init_db()
        print("데이터베이스 초기화가 완료되었습니다.")
    except Exception as e:
        print(f"데이터베이스 초기화 중 오류가 발생했습니다: {e}")
    finally:
        db_manager.close()

if __name__ == "__main__":
    init_database() 