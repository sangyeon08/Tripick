import os
import datetime

class AuthManager:
    
    def __init__(self, sql_file="users.sql"):
        self.sql_file = sql_file
        self.users = {}
        self.load_from_sql()

    def load_from_sql(self):
        if not os.path.exists(self.sql_file):
            self.create_initial_sql()
            return
        
        file = open(self.sql_file, 'r', encoding='utf-8')
        content = file.read()
        file.close()
        
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            
            # INSERT 문만 처리 (사용자 데이터가 들어있는 줄)
            if line.startswith('INSERT INTO users'):
                # VALUES 뒷부분 찾기
                if 'VALUES' in line:
                    # VALUES 뒷부분만 빼오기
                    values_part = line.split('VALUES')[1]
                    values_part = values_part.strip()
                    values_part = values_part.strip('();')
                    
                    parts = values_part.split(',')
                    
                    clean_parts = []
                    for part in parts:
                        part = part.strip()
                        part = part.strip("'")
                        clean_parts.append(part)
                    
                    # 3개 부분이 있어야 함 (아이디, 비밀번호, 가입날짜)
                    if len(clean_parts) >= 3:
                        username = clean_parts[0]
                        password = clean_parts[1]
                        created_at = clean_parts[2]
                        
                        # 딕셔너리에 저장
                        self.users[username] = {
                            'password': password,
                            'created_at': created_at
                        }

    def create_initial_sql(self):
        """처음 SQL 파일 만들기 (파일이 없을 때 쓰려고)"""
        sql_text = """-- Tripick Users Database
-- Created: 2025-11-17

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at TEXT NOT NULL
);

-- User Data (INSERT statements will be added below)
"""
        
        file = open(self.sql_file, 'w', encoding='utf-8')
        file.write(sql_text)
        file.close()

    def save_to_sql(self):
        # SQL 파일 헤더 작성 - 이건 왜 필요하지? -> 사용자 데이터 덮어쓰려고
        sql_text = """-- Tripick Users Database
-- Last Updated: 2025-11-17

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at TEXT NOT NULL
);

-- Clear existing data
DELETE FROM users;

-- User Data
"""
        
        # 각 사용자 정보를 INSERT 문으로 만들기
        for username in self.users:
            password = self.users[username]['password']
            created_at = self.users[username]['created_at']
            
            # INSERT 문
            insert_line = "INSERT INTO users (username, password, created_at) VALUES ('"
            insert_line = insert_line + username + "', '"
            insert_line = insert_line + password + "', '"
            insert_line = insert_line + created_at + "');\n"
            
            sql_text = sql_text + insert_line
        
        file = open(self.sql_file, 'w', encoding='utf-8')
        file.write(sql_text)
        file.close()

    def register(self, username, password):
        if username == "" or password == "":
            return False, "아이디와 비밀번호를 입력해주세요."
        
        if len(username) < 3:
            return False, "아이디는 3자 이상이어야 합니다."
        
        if len(password) < 4:
            return False, "비밀번호는 4자 이상이어야 합니다."

        if username in self.users:
            return False, "이미 존재하는 아이디입니다."

        # 딕셔너리에 추가
        self.users[username] = {
            'password': password,
            'created_at': datetime.date.today().isoformat()  
            # 올.. 개신기하네. 원래 고정 날짜로 하려고 했는데. isoformat은 - 넣어줌.
        }
        
        self.save_to_sql()
        
        return True, "회원가입이 완료되었습니다!"

    def login(self, username, password):
        """로그인 처리"""
        if username == "" or password == "":
            return False, "아이디와 비밀번호를 입력해주세요."

        if username not in self.users:
            return False, "아이디 또는 비밀번호가 일치하지 않습니다."
        
        saved_password = self.users[username]['password']
        
        if password == saved_password:
            message = username + "님, 환영합니다!"
            return True, message
        else:
            return False, "아이디 또는 비밀번호가 일치하지 않습니다."

    def user_exists(self, username):
        if username in self.users:
            return True
        else:
            return False