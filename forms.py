from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TextForm(FlaskForm):
    text = StringField('Text', validators=[DataRequired()])
    submit = SubmitField('Speech')