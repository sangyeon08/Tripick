import hashlib
from datetime import datetime
import os


class AuthManager:
    def __init__(self, sql_file="users.sql"):
        self.sql_file = sql_file
        self.users = {}
        self.load_from_sql()

    def load_from_sql(self):
        if not os.path.exists(self.sql_file):
            self.create_initial_sql()
            return
        
        try:
            with open(self.sql_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            for line in content.split('\n'):
                if line.strip().startswith('INSERT INTO users'):
                    if 'VALUES' in line:
                        values_part = line.split('VALUES')[1].strip()
                        values_part = values_part.strip('();')
                        parts = [p.strip().strip("'") for p in values_part.split(',')]
                        if len(parts) >= 3:
                            username = parts[0]
                            password = parts[1]
                            created_at = parts[2]
                            self.users[username] = {
                                'password': password,
                                'created_at': created_at
                            }
        except Exception as e:
            print(f"SQL 파일 로드 중 오류: {e}")
            self.create_initial_sql()

    def create_initial_sql(self):
        initial_content = """-- Tripick Users Database
-- Created: {}

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at TEXT NOT NULL
);

-- User Data (INSERT statements will be added below)
""".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        
        try:
            with open(self.sql_file, 'w', encoding='utf-8') as f:
                f.write(initial_content)
        except Exception as e:
            print(f"SQL 파일 생성 중 오류: {e}")

    def save_to_sql(self):
        sql_content = """-- Tripick Users Database
-- Last Updated: {}

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at TEXT NOT NULL
);

-- Clear existing data
DELETE FROM users;

-- User Data
""".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        
        for username, data in self.users.items():
            password = data['password']
            created_at = data['created_at']
            sql_content += f"INSERT INTO users (username, password, created_at) VALUES ('{username}', '{password}', '{created_at}');\n"
        
        try:
            with open(self.sql_file, 'w', encoding='utf-8') as f:
                f.write(sql_content)
        except Exception as e:
            print(f"SQL 파일 저장 중 오류: {e}")

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username, password):
        if not username or not password:
            return False, "아이디와 비밀번호를 입력해주세요."
        
        if len(username) < 3:
            return False, "아이디는 3자 이상이어야 합니다."
        
        if len(password) < 4:
            return False, "비밀번호는 4자 이상이어야 합니다."

        if username in self.users:
            return False, "이미 존재하는 아이디입니다."

        try:
            hashed_pw = self.hash_password(password)
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            self.users[username] = {
                'password': hashed_pw,
                'created_at': created_at
            }
            
            self.save_to_sql()
            
            return True, "회원가입이 완료되었습니다!"
        
        except Exception as e:
            return False, f"오류가 발생했습니다: {str(e)}"

    def login(self, username, password):

        if not username or not password:
            return False, "아이디와 비밀번호를 입력해주세요."

        try:
            if username not in self.users:
                return False, "아이디 또는 비밀번호가 일치하지 않습니다."
            
            hashed_pw = self.hash_password(password)
            
            if self.users[username]['password'] == hashed_pw:
                return True, f"{username}님, 환영합니다!"
            else:
                return False, "아이디 또는 비밀번호가 일치하지 않습니다."
        
        except Exception as e:
            return False, f"오류가 발생했습니다: {str(e)}"

    def user_exists(self, username):
        return username in self.users