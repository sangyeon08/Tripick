import os

class FavoriteManager:
    
    def __init__(self, filename="favorites.txt"):
        """초기화: 파일 경로 설정 및 즐겨찾기 로드"""
        self.favorites = []
        self.filename = filename
        self.load()

    def add(self, destination_name):
        if destination_name in self.favorites:
            print("이미 즐겨찾기에 있는 여행지입니다.")
            return False
        
        self.favorites.append(destination_name)
        print(destination_name + " 즐겨찾기에 추가됨")
        
        self.save()
        return True

    def remove(self, destination_name):
        if destination_name not in self.favorites:
            print("해당 이름이 즐겨찾기에 없습니다.")
            return False
        
        self.favorites.remove(destination_name)
        print(destination_name + " 즐겨찾기에서 삭제됨")
        
        self.save()
        return True

    def show(self):
        if len(self.favorites) == 0:
            print("즐겨찾기 비어있음")
            return

        print("\n=== 즐겨찾기 목록 ===")
        for name in self.favorites:
            print("- " + name)

    def save(self):
        file = open(self.filename, "w", encoding="utf-8")
        
        for name in self.favorites:
            file.write(name + "\n")
        
        file.close()

    def load(self):
        if not os.path.exists(self.filename):
            self.favorites = []
            return
        
        file = open(self.filename, "r", encoding="utf-8")
        lines = file.readlines()
        file.close()
        
        self.favorites = []
        
        for line in lines:
            name = line.strip()
            
            if name != "":
                self.favorites.append(name)