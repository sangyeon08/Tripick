class Destination:
    """여행지 정보를 담는 클래스"""

    def __init__(self, name, country, keywords, description=""):
        self.name = name               # 여행지 이름
        self.country = country         # 나라 이름
        self.keywords = keywords       # 여행지 특징 키워드 리스트
        self.description = description # 간단한 소개 문장(선택)

    def __str__(self):
        """객체를 문자열로 출력할 때 사용"""
        keyword_text = ", ".join(self.keywords)
        return f"{self.name} ({self.country}) - {keyword_text}"

    def match_keywords(self, user_keywords):
        """사용자 키워드와 일치하는 개수를 반환"""
        count = 0
        for keyword in user_keywords:
            if keyword in self.keywords:
                count += 1
        return count

    def has_keyword(self, keyword):
        """특정 키워드를 포함하고 있는지 확인"""
        return keyword in self.keywords

    def short_info(self):
        """한 줄 요약 정보 반환"""
        if self.description:
            return f"{self.name} - {self.description}"
        else:
            return f"{self.name} - 키워드 기반 추천 여행지"
