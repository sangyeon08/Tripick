class Destination:

    def __init__(self, name, country, keywords, description=""):
        self.name = name
        self.country = country
        self.keywords = keywords
        self.description = description

    def __str__(self):
        keyword_text = ", ".join(self.keywords)
        
        result = self.name + " (" + self.country + ") - " + keyword_text
        return result

    def match_keywords(self, user_keywords):
        count = 0
        
        for keyword in user_keywords:
            if keyword in self.keywords:
                count = count + 1
        
        return count

    def has_keyword(self, keyword):
        if keyword in self.keywords:
            return True
        else:
            return False

    def short_info(self):
        # 설명이 있으면 쓰고
        if self.description != "":
            result = self.name + " - " + self.description
        else:
            # 없으면 기본
            result = self.name + " - 키워드 기반 추천 여행지"
        
        return result