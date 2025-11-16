from flask import Flask, render_template, request, redirect, url_for, session, flash
from keyword_mg import Keyword_mg
from recommender import Recommender
from favorite import FavoriteManager
from auth import AuthManager
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
app.secret_key = "tripick_secret_key_2025"

km = Keyword_mg()
rec = Recommender()
fav = FavoriteManager()
auth = AuthManager()


@app.route("/")
def index():
    if "username" in session:
        return redirect(url_for("home"))
    return redirect(url_for("register"))


@app.route("/home")
def home():
    if "username" not in session:
        flash("로그인이 필요한 서비스입니다.", "error")
        return redirect(url_for("login"))
    
    return render_template(
        "home.html",
        valid_keywords=km.valid_keywords,
        username=session.get("username")
    )


@app.route("/recommend", methods=["GET", "POST"])
def recommend():
    if "username" not in session:
        flash("로그인이 필요한 서비스입니다.", "error")
        return redirect(url_for("login"))
    
    if request.method == "GET":
        return redirect(url_for("home"))
    
    keywords_text = request.form.get("keywords", "")
    parsed_keywords = km.process_input(keywords_text)
    results = rec.recommend(parsed_keywords)

    return render_template(
        "recommend.html",
        keywords_text=keywords_text,
        parsed_keywords=parsed_keywords,
        results=results,
        username=session.get("username")
    )


@app.route("/favorites")
def favorites():
    if "username" not in session:
        flash("로그인이 필요한 서비스입니다.", "error")
        return redirect(url_for("login"))
    
    return render_template(
        "favorites.html",
        favorites=fav.favorites,
        username=session.get("username")
    )


@app.route("/favorite/add", methods=["GET", "POST"])
def add_favorite():
    if "username" not in session:
        flash("로그인이 필요한 서비스입니다.", "error")
        return redirect(url_for("login"))
    
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if name:
            fav.add(name)
        if request.referrer:
            return redirect(request.referrer)
        return redirect(url_for("favorites"))
    
    return redirect(url_for("favorites"))


@app.route("/favorite/delete", methods=["GET", "POST"])
def delete_favorite():
    if "username" not in session:
        flash("로그인이 필요한 서비스입니다.", "error")
        return redirect(url_for("login"))
    
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if name:
            fav.remove(name)
        if request.referrer:
            return redirect(request.referrer)
        return redirect(url_for("favorites"))
    
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
        is_correct=is_correct,
        username=session.get("username")
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        
        success, message = auth.register(username, password)
        
        if success:
            flash(message, "success")
            return redirect(url_for("login"))
        else:
            flash(message, "error")
    
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        
        success, message = auth.login(username, password)
        
        if success:
            session["username"] = username
            flash(message, "success")
            return redirect(url_for("home"))
        else:
            flash(message, "error")
    
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    session.pop('_flashes', None)
    flash("로그아웃되었습니다.", "success")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)