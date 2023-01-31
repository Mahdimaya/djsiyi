from flask import Blueprint ,render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("snowy.html")

@views.route('/snowybook')
def snowybook():
    return render_template("snowy.html")

@views.route('/mystery')
def mystery():
    return render_template("mystery.html")

@views.route('/action')
def action():
    return render_template("action.html")

@views.route('/thriller')
def thriller():
    return render_template("thriller.html")

@views.route('/sciencefiction')
def sciencefiction():
    return render_template("sci-fi.html")

@views.route('/rommance')
def rommance():
    return render_template("rommance.html")

@views.route('/novel')
def novel():
    return render_template("novel.html")

@views.route('/drame')
def drame():
    return render_template("drame.html")

@views.route('/darkfantasy')
def darkfantasy():
    return render_template("dark.html")

@views.route('/crime')
def crime():
    return render_template("crime.html")

@views.route('/commingofage')
def commingofage():
    return render_template("commage.html")

@views.route('/biography')
def biography():
    return render_template("biography.html")

@views.route('/manga')
def manga():
    return render_template("manga.html")
    
