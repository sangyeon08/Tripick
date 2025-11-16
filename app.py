from flask import Flask, render_template, request, redirect, url_for
from keyword_mg import Keyword_mg
from recommender import Recommender
from favorite import FavoriteManager
import random

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

km = Keyword_mg()
rec = Recommender()
fav = FavoriteManager()


@app.route("/")
def home():
    return render_template(
        "home.html",
        valid_keywords=km.valid_keywords
    )


@app.route("/recommend", methods=["POST"])
def recommend():
    keywords_text = request.form.get("keywords", "")
    parsed_keywords = km.process_input(keywords_text)
    results = rec.recommend(parsed_keywords)

    return render_template(
        "recommend.html",
        keywords_text=keywords_text,
        parsed_keywords=parsed_keywords,
        results=results,
    )


@app.route("/favorites")
def favorites():
    return render_template(
        "favorites.html",
        favorites=fav.favorites
    )


@app.route("/favorite/add", methods=["POST"])
def add_favorite():
    name = request.form.get("name", "").strip()
    if name:
        fav.add(name)
    if request.referrer:
        return redirect(request.referrer)
    return redirect(url_for("favorites"))


@app.route("/favorite/delete", methods=["POST"])
def delete_favorite():
    name = request.form.get("name", "").strip()
    if name:
        fav.remove(name)
    if request.referrer:
        return redirect(request.referrer)
    return redirect(url_for("favorites"))


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    message = None
    is_correct = None

    if request.method == "POST":
        prev_country = request.form.get("country")
        answer = request.form.get("answer", "").strip()
        correct_answer = CAPITALS.get(prev_country)
        if correct_answer:
            if answer == correct_answer:
                is_correct = True
                message = f"정답! {prev_country}의 수도는 {correct_answer}입니다."
            else:
                is_correct = False
                message = f"오답! {prev_country}의 수도는 {correct_answer}입니다. 입력한 답: {answer}"

    country = random.choice(list(CAPITALS.keys()))
    capital = CAPITALS[country]

    return render_template(
        "quiz.html",
        country=country,
        capital=capital,
        message=message,
        is_correct=is_correct
    )


if __name__ == "__main__":
    app.run(debug=True)