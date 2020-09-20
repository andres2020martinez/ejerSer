'''from flask import Flask


app = Flask(__name__)


@app.route("/")
def home_page():
    return "My movie collection"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)'''

'''from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)'''

'''from datetime import datetime

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=day_name)

@app.route("/movies")
def movies_page():
    return render_template("movies.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)'''

'''from flask import Flask

import views


def create_app():
    app = Flask(__name__)

    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/movies", view_func=views.movies_page)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8080, debug=True)'''

from flask import Flask

import views
from database import Database
from movie import Movie


def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/movies", view_func=views.movies_page)
    app.add_url_rule("/movies/<int:movie_key>", view_func=views.movie_page)

    db = Database()
    db.add_movie(Movie("Slaughterhouse-Five", year=1972))
    db.add_movie(Movie("The Shining"))
    app.config["db"] = db

    return app


if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port)