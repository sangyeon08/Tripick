class Keyword_mg:
    #키워드를 관리하는 클래스

    def __init__(self):
        # 일단 몇 개만 추가
        self.valid_keywords = [
            "바다", "산", "휴양지", "도시", "조용한"
        ]
        #더 많은 키워드 추가하자

    def process_input(self, user_input):
        #사용자 입력을 키워드 리스트로 변환
        # 일단 쉼표로만 구분
        keywords = user_input.split(',')

        result = []
        for keyword in keywords:
            keyword = keyword.strip()
            if keyword in self.valid_keywords:
                result.append(keyword)

        return result

    # TODO: 키워드 유사어 처리 기능 추가 예정
    # TODO: 자동완성 기능 나중에 구현