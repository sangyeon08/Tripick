class Keyword_mg:
    
    def __init__(self):
        self.valid_keywords = [
            "바다", "산", "휴양지", "도시", "조용한"
        ]

        # 비슷하게 처리할 애들
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
            
            if keyword == "":
                continue

            if keyword in self.synonyms:
                keyword = self.synonyms[keyword]

            if keyword in self.valid_keywords:
                if keyword not in result:
                    result.append(keyword)
            else:
                invalid.append(keyword)

        if len(invalid) > 0:
            print("무시하는 애들:", invalid)

        return result

    def show_help(self):
        print("\n되는 애들:")
        for keyword in self.valid_keywords:
            print("-", keyword)

    def suggest(self, prefix):
        prefix = prefix.strip()
        
        if prefix == "":
            return []

        suggestions = []
        
        for keyword in self.valid_keywords:
            if keyword.startswith(prefix):
                suggestions.append(keyword)
        
        return suggestions