from destination import Destination


class Recommender:
    #여행지 추천 시스템 - 아직 개발 중

    def __init__(self):
        self.destinations = []
        self.load_destinations()

    def load_destinations(self):
        #여행지 데이터 로드 - 일단 몇 개만 추가
        #restcountries  라는 api가 있네? 이거 쓰는 것도 좋겠다
        # 테스트용으로 4개만 넣어둠
        self.destinations = [
            Destination("몰디브", "몰디브", ["바다", "휴양지"]),
            Destination("제주도", "대한민국", ["바다", "산", "휴양지"]),
            Destination("교토", "일본", ["도시", "조용한"]),
            Destination("발리", "인도네시아", ["바다", "휴양지"])
        ]
        #더 많은 여행지 추가 필요
        #나중에 파일에서 읽어오도록 변경

    def recommend(self, keywords):
        """키워드 기반 추천 - 기본 기능만"""
        if not keywords:
            return []

        # 일단 매칭되는 것만 찾기
        results = []
        for dest in self.destinations:
            score = dest.match_keywords(keywords)
            if score > 0:
                results.append(dest)

        #점수 순으로 정렬하는 기능 추가 예정
        #상위 3개만 선택하는 로직 구현 필요.. 아ㅏㅏ앙락..앍....

        return results