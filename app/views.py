from flask import render_template, request, redirect, url_for
from app import app
from .request import get_movies, get_movie, search_movie

#Home view
@app.route('/')
def index():
    popular_movies = get_movies('popular')
    upcoming_movies = get_movies('upcoming')
    now_showing_movies = get_movies('now_playing')
    title = 'Home - Welcome To The Best Movie Review webiste Online'
    message = 'Welcome To The Best Movie Review webiste Online'

    search_movie = request.args.get('movie_query')
    if search_movie:
        return redirect(url_for('search', movie_name = search_movie))
    else:
        return render_template('index.html', title = title, message = message, popular = popular_movies, upcoming = upcoming_movies, now_showing = now_showing_movies)

#Movie details view
@app.route('/movie/<int:id>')
def movie(id):
    movie = get_movie(id)
    title = f'{movie.title}'
    return render_template('movie.html', title = title, movie = movie)

#Search view
@app.route('/search/<movie_name>')
def search(movie_name):
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'Search results for {movie_name}'
    return render_template('search.html', movies = searched_movies)