from flask import Flask, render_template, request, redirect, url_for
from keyword_mg import Keyword_mg
from recommender import Recommender
from favorite import FavoriteManager
import random

# 웹용 수도 퀴즈 데이터 (20개국)
CAPITALS = {
    "대한민국": "서울",
    "일본": "도쿄",
    "중국": "베이징",
    "대만": "타이베이",
    "태국": "방콕",
    "베트남": "하노이",
    "인도네시아": "자카르타",
    "말레이시아": "쿠알라룸푸르",
    "싱가포르": "싱가포르",
    "필리핀": "마닐라",
    "미국": "워싱턴 D.C.",
    "캐나다": "오타와",
    "멕시코": "멕시코시티",
    "영국": "런던",
    "프랑스": "파리",
    "독일": "베를린",
    "이탈리아": "로마",
    "스페인": "마드리드",
    "호주": "캔버라",
    "뉴질랜드": "웰링턴",
}

app = Flask(__name__)

# 공용 객체 (한 번만 만들고 계속 사용)
km = Keyword_mg()
rec = Recommender()
fav = FavoriteManager()


@app.route("/", methods=["GET", "POST"])
def index():
    """메인 페이지: 키워드 입력 + 추천 결과 + 즐겨찾기"""
    keywords_text = ""
    parsed_keywords = []
    results = []

    if request.method == "POST":
        keywords_text = request.form.get("keywords", "")
        parsed_keywords = km.process_input(keywords_text)
        results = rec.recommend(parsed_keywords)

    return render_template(
        "index.html",
        keywords_text=keywords_text,
        parsed_keywords=parsed_keywords,
        results=results,
        favorites=fav.favorites,
        valid_keywords=km.valid_keywords
    )


@app.route("/favorite/add", methods=["POST"])
def add_favorite():
    """즐겨찾기 추가"""
    name = request.form.get("name", "").strip()
    if name:
        fav.add(name)
    return redirect(url_for("index"))


@app.route("/favorite/delete", methods=["POST"])
def delete_favorite():
    """즐겨찾기 삭제"""
    name = request.form.get("name", "").strip()
    if name:
        fav.remove(name)
    return redirect(url_for("index"))


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    """
    수도 퀴즈 페이지.
    POST로 답을 받으면 결과 메시지 보여주고,
    항상 새로운 문제를 하나 더 내줌.
    """
    message = None

    if request.method == "POST":
        prev_country = request.form.get("country")
        answer = request.form.get("answer", "").strip()
        correct = CAPITALS.get(prev_country)
        if correct:
            if answer == correct:
                message = f"정답입니다! {prev_country}의 수도는 {correct}입니다."
            else:
                message = f"틀렸어요. {prev_country}의 수도는 {correct}입니다."

    # 다음 문제 출제
    country = random.choice(list(CAPITALS.keys()))
    capital = CAPITALS[country]
    hint = capital[0] + "*" * (len(capital) - 1)

    return render_template(
        "quiz.html",
        country=country,
        hint=hint,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)