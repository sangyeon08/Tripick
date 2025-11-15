class CapitalQuiz:
    #수도 맞히기 퀴즈

    def __init__(self):
        # 일단 몇 개만
        self.capitals = {
            "대한민국": "서울",
            "일본": "도쿄",
            "프랑스": "파리"
        }
        # TODO: 더 많은 국가 추가

    def start(self):
        #퀴즈 시작 - 기본만 동작
        print("\n=== 수도 맞히기 ===")
        print("(개발 중입니다...)")

        # 일단 하나만 물어봄
        country = "대한민국"
        answer = input(f"{country}의 수도는? ")

        if answer == self.capitals[country]:
            print("정답!")
        else:
            print(f"틀렸습니다. 정답: {self.capitals[country]}")

        #여러 문제 내는 기능
        #힌트 기능
        #점수 계산
        #랜덤 선택 기능