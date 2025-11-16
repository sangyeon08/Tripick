class Keyword_mg:
    """키워드를 관리하는 클래스"""

    def __init__(self):
        # 기본 키워드
        self.valid_keywords = [
            "바다", "산", "휴양지", "도시", "조용한"
        ]

        # 간단한 유사어 사전
        self.synonyms = {
            "해변": "바다",
            "휴식": "휴양지",
            "힐링": "휴양지",
            "시끄러운 도시": "도시",
            "한적한": "조용한",
        }

    def process_input(self, user_input):
        """
        사용자 입력 문자열을 키워드 리스트로 변환.
        쉼표(,) 기준으로 나누고, 유효한 키워드만 반환.
        """
        keywords = user_input.split(',')

        result = []
        invalid = []

        for keyword in keywords:
            keyword = keyword.strip()
            if not keyword:
                continue

            # 유사어를 기본 키워드로 변환
            if keyword in self.synonyms:
                keyword = self.synonyms[keyword]

            if keyword in self.valid_keywords:
                if keyword not in result:   # 중복 제거
                    result.append(keyword)
            else:
                invalid.append(keyword)

        if invalid:
            print("사용할 수 없는 키워드(무시됨):", invalid)

        return result

    def show_help(self):
        """사용 가능한 키워드 안내 (콘솔용)"""
        print("\n사용 가능한 키워드 목록:")
        for kw in self.valid_keywords:
            print("-", kw)

    def suggest(self, prefix):
        """입력한 앞부분으로 시작하는 키워드 추천"""
        prefix = prefix.strip()
        if not prefix:
            return []

        suggestions = []
        for kw in self.valid_keywords:
            if kw.startswith(prefix):
                suggestions.append(kw)
        return suggestions
