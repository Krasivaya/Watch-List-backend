from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

def ReviewForm(FlaskForm):
    title = StringField('Movie title', validators = [Required()])
    review = TextAreaField('Moview review', validators = [Required()])
    submit = SubmitField('Submit')