class Destination:
    #여행지 정보를 담는 클래스

    def __init__(self, name, country, keywords):
        self.name = name
        self.country = country
        self.keywords = keywords
        #tags 기능은 다음에 추가하겟지..?

    def __str__(self):
        # 간단한 출력만 구현
        return f"{self.name} ({self.country})"

    def match_keywords(self, user_keywords):
        #사용자 키워드와 일치하는 개수 반환
        count = 0
        for keyword in user_keywords:
            if keyword in self.keywords:
                count += 1
        return count

    #나중에 태그 관련 메소드 추가하자