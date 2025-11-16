from destination import Destination


class Recommender:

    def __init__(self, filename="destinations.txt"):
        self.destinations = []
        self.filename = filename
        self.load_destinations()

    def load_destinations(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                self.destinations = []
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    parts = line.split("|")
                    if len(parts) != 3:
                        continue
                    name = parts[0].strip()
                    country = parts[1].strip()
                    kw_text = parts[2].strip()
                    keywords = [k.strip() for k in kw_text.split(",") if k.strip()]
                    dest = Destination(name, country, keywords)
                    self.destinations.append(dest)

            if not self.destinations:
                self._load_default_destinations()

        except FileNotFoundError:
            self._load_default_destinations()
        except Exception as e:
            print("여행지 데이터를 읽는 중 오류 발생:", e)
            self._load_default_destinations()

    def _load_default_destinations(self):
        self.destinations = [
            Destination("몰디브", "몰디브", ["바다", "휴양지"], "에메랄드빛 바다와 리조트"),
            Destination("제주도", "대한민국", ["바다", "산", "휴양지"], "국내에서 즐기는 섬 여행"),
            Destination("교토", "일본", ["도시", "조용한"], "조용한 사찰과 전통 거리"),
            Destination("발리", "인도네시아", ["바다", "휴양지"], "휴양과 서핑을 즐기기 좋은 섬"),
            Destination("파리", "프랑스", ["도시", "조용한"], "예술과 카페 문화의 도시"),
            Destination("방콕", "태국", ["도시", "휴양지"], "야시장과 맛집이 많은 도시"),
        ]

    def recommend(self, keywords):
        if not keywords:
            return []

        scored = []
        for dest in self.destinations:
            score = dest.match_keywords(keywords)
            if score > 0:
                scored.append((dest, score))

        if not scored:
            return []

        scored.sort(key=lambda x: x[1], reverse=True)
        top = scored[:3]
        results = [item[0] for item in top]
        return results

    def add_destination(self, name, country, keywords):
        kw_text = ",".join(keywords)

        try:
            with open(self.filename, "a", encoding="utf-8") as f:
                line = f"{name}|{country}|{kw_text}\n"
                f.write(line)
            print(f"여행지 '{name}' 가(이) 파일에 추가되었습니다.")
        except Exception as e:
            print("여행지를 파일에 추가하는 중 오류 발생:", e)

        self.load_destinations()
