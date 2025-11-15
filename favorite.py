class FavoriteManager:
    """즐겨찾기 관리 클래스"""

    def __init__(self):
        self.favorites = []
        #파일 저장/불러오기는 아직 안 됨 ㅎㅎ

    def add(self, destination_name):
        """즐겨찾기 추가"""
        if destination_name not in self.favorites:
            self.favorites.append(destination_name)
            print(f"'{destination_name}' 추가됨")
            return True
        else:
            print("이미 있음")
            return False

    def show(self):
        """즐겨찾기 목록 출력"""
        if not self.favorites:
            print("즐겨찾기 비어있음")
            return

        print("\n=== 즐겨찾기 ===")
        for name in self.favorites:
            print(f"- {name}")

    #파일 저장 기능 구현 필요
    #파일 불러오기 기능 구현 필요
    #삭제 기능도 만들어야 함;;