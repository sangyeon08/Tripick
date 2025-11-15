from keyword_mg import Keyword_mg
from recommender import Recommender
from favorite import FavoriteManager
from quiz import CapitalQuiz


def main():
    """메인 함수"""

    print("=" * 40)
    print("   Tripick - 여행지 추천 (개발 중)")
    print("=" * 40)

    # 초기화
    km = Keyword_mg()
    rec = Recommender()
    fav = FavoriteManager()

    print("사용 가능한 키워드:", km.valid_keywords)

    while True:
        print("\n1. 여행지 추천")
        print("2. 즐겨찾기")
        print("3. 퀴즈 (테스트)")
        print("4. 종료")

        choice = input("선택: ")

        if choice == '1':
            # 추천 기능
            user_input = input("키워드 입력 (쉼표로 구분): ")
            keywords = km.process_input(user_input)

            print(f"입력된 키워드: {keywords}")

            results = rec.recommend(keywords)

            if results:
                print("\n추천 결과:")
                for i, dest in enumerate(results):
                    print(f"{i + 1}. {dest}")

                # 즐겨찾기 추가
                add = input("즐겨찾기 추가? (번호): ")
                if add.isdigit():
                    idx = int(add) - 1
                    if 0 <= idx < len(results):
                        fav.add(results[idx].name)
            else:
                print("추천 결과 없음")

        elif choice == '2':
            fav.show()

        elif choice == '3':
            quiz = CapitalQuiz()
            quiz.start()

        elif choice == '4':
            print("종료")
            break

        #메뉴 더 예쁘게 만들기
        #에러 처리 추가
        #이스터에그 숨기기


if __name__ == "__main__":
    main()