class CapitalQuiz:
    def __init__(self):
        self.capitals = {
            "대한민국": "서울",
            "일본": "도쿄",
            "프랑스": "파리"
        }
    def start(self):

        print("\n=== 수도 맞히기 ===")
        print("(개발 중입니다...)")

        country = "대한민국"
        answer = input(f"{country}의 수도는? ")

        if answer == self.capitals[country]:
            print("정답!")
        else:
            print(f"틀렸습니다. 정답: {self.capitals[country]}")