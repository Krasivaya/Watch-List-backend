from flask import render_template
from app import app
from .request import get_movies

#Views
@app.route('/')
def index():
    popular_movies = get_movies('popular')
    title = 'Home - Welcome To The Best Movie Review webiste Online'
    message = 'Welcome To The Best Movie Review webiste Online'
    return render_template('index.html', title = title, message = message, popular = popular_movies)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    title = 'Movie'
    return render_template('movie.html', title = title, id = movie_id)