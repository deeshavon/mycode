# An object of Flask class is our app
from flask import Flask, render_template
from flask import jsonify
import random

# module (__name__) as argument
app = Flask(__name__)


# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/genres")
def movie():
    return random.choice(genres)


@app.route("/leaving")
def titles():
    return "Oh no! My favorite binge title is booted!"


genres = {
    "1": "Biography",
    "2": "Film Noir",
    "3": "Game Show",
    "4": "Musical",
    "5": "Sport",
    "6": "Short",
    "7": "Adult",
    "12": "Adventure",
    "14": "Fantasy",
    "16": "Animation",
    "18": "Drama",
    "27": "Horror",
    "28": "Action",
    "35": "Comedy",
    "36": "History",
    "37": "Western",
    "53": "Thriller",
    "80": "Crime",
    "99": "Documentary",
    "878": "Science Fiction",
    "9648": "Mystery",
    "10402": "Music",
    "10749": "Romance",
    "10751": "Family",
    "10752": "War",
    "10763": "News",
    "10764": "Reality",
    "10767": "Talk Show"
}


@app.route("/")
def index():
    # jsonify returns legal JSON
    return jsonify()

@app.route("/")
def index():
    return render_template("howdy.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)  # runs the application
    # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE
