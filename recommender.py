from destination import Destination

class Recommender:
    
    def __init__(self, filename="data/destinations.txt"):
        self.destinations = []
        self.filename = filename
        self.load_destinations()

    def load_destinations(self):
        self.destinations = []
        
        file = open(self.filename, "r", encoding="utf-8")
        lines = file.readlines()
        file.close()
        
        for line in lines:
            line = line.strip()  # 양공백 제거 개신기하네
            
            if line == "" or line.startswith("#"):
                continue
            
            # 형식: 이름|나라|키워드1,키워드2, 등등ㄷ으
            parts = line.split("|")
            
            # 3개 부분이 아니면 건너뛰어!
            if len(parts) != 3:
                continue
            
            # 각 부분 빼오기
            name = parts[0].strip()
            country = parts[1].strip()
            keywords_text = parts[2].strip()
            
            # 키워드를 쉼표로 나누기
            keywords = []
            for keyword in keywords_text.split(","):
                keyword = keyword.strip()
                if keyword != "":
                    keywords.append(keyword)
            
            # Destination 객체 만들어서 리스트에 추가
            dest = Destination(name, country, keywords)
            self.destinations.append(dest)

    def recommend(self, user_keywords):
        if len(user_keywords) == 0:
            return []

        scored_list = []  # (여행지, 점수) 구조임 헷갈리지 X
        
        for dest in self.destinations:
            score = 0
            for keyword in user_keywords:
                if keyword in dest.keywords:
                    score = score + 1
            
            if score > 0:
                scored_list.append((dest, score))

        # 결과 없으면 빈 리스트로
        if len(scored_list) == 0:
            return []

        # 점수 높은 순으로 정렬
        # lambda x: x[1] -- 튜플의 두 번째 요소(점수)로 정렬
        # reverse=True: 큰 것부터 (내림차순) ...개신기하네 오케이!
        scored_list.sort(key=lambda x: x[1], reverse=True)
        
        top_3 = scored_list[:3]
        
        # 여행지 객체만 가져오기
        results = []
        for item in top_3:
            dest = item[0]
            results.append(dest)
        
        return results

    def add_destination(self, name, country, keywords):
        keywords_text = ",".join(keywords)
        
        file = open(self.filename, "a", encoding="utf-8")
        new_line = name + "|" + country + "|" + keywords_text + "\n"
        file.write(new_line)
        file.close()
        
        print(name + " 가(이) 파일에 추가되었습니다.")
        
        self.load_destinations()