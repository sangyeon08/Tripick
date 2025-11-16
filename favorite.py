class FavoriteManager:
    """즐겨찾기 관리 클래스"""

    def __init__(self, filename="favorites.txt"):
        self.favorites = []
        self.filename = filename
        self.load()

    def add(self, destination_name):
        """즐겨찾기 추가"""
        if destination_name not in self.favorites:
            self.favorites.append(destination_name)
            print(f"'{destination_name}' 즐겨찾기에 추가됨")
            self.save()
            return True
        else:
            print("이미 즐겨찾기에 있는 여행지입니다.")
            return False

    def remove(self, destination_name):
        """즐겨찾기 삭제"""
        if destination_name in self.favorites:
            self.favorites.remove(destination_name)
            print(f"'{destination_name}' 즐겨찾기에서 삭제됨")
            self.save()
            return True
        else:
            print("해당 이름이 즐겨찾기에 없습니다.")
            return False

    def show(self):
        """즐겨찾기 목록 출력 (콘솔용)"""
        if not self.favorites:
            print("즐겨찾기 비어있음")
            return

        print("\n=== 즐겨찾기 목록 ===")
        for name in self.favorites:
            print(f"- {name}")

    def save(self):
        """즐겨찾기 목록을 파일에 저장"""
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                for name in self.favorites:
                    f.write(name + "\n")
        except Exception as e:
            print("즐겨찾기를 저장하는 중 오류 발생:", e)

    def load(self):
        """파일에서 즐겨찾기 목록 불러오기"""
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                self.favorites = []
                for line in f:
                    name = line.strip()
                    if name:
                        self.favorites.append(name)
        except FileNotFoundError:
            self.favorites = []
        except Exception as e:
            print("즐겨찾기를 불러오는 중 오류 발생:", e)
            self.favorites = []
