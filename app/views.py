from flask import render_template
from app import app

#Views
@app.route('/')
def index():
    title = 'Home - Welcome tothe best Movie Review webiste Online'
    message = 'Hello world!'
    return render_template('index.html', title = title, message = message)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    title = 'Movie'
    return render_template('movie.html', title = title, id = movie_id)