class Keyword_mg:
    def __init__(self):
        self.valid_keywords = [
            "바다", "산", "휴양지", "도시", "조용한"
        ]

        self.synonyms = {
            "해변": "바다",
            "휴식": "휴양지",
            "힐링": "휴양지",
            "시끄러운 도시": "도시",
            "한적한": "조용한",
        }

    def process_input(self, user_input):
        keywords = user_input.split(',')

        result = []
        invalid = []

        for keyword in keywords:
            keyword = keyword.strip()
            if not keyword:
                continue

            if keyword in self.synonyms:
                keyword = self.synonyms[keyword]

            if keyword in self.valid_keywords:
                if keyword not in result:
                    result.append(keyword)
            else:
                invalid.append(keyword)

        if invalid:
            print("사용할 수 없는 키워드(무시됨):", invalid)

        return result

    def show_help(self):
        print("\n사용 가능한 키워드 목록:")
        for kw in self.valid_keywords:
            print("-", kw)

    def suggest(self, prefix):
        prefix = prefix.strip()
        if not prefix:
            return []

        suggestions = []
        for kw in self.valid_keywords:
            if kw.startswith(prefix):
                suggestions.append(kw)
        return suggestions
