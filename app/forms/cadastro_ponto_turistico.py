from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DecimalField
from wtforms.validators import DataRequired, NumberRange

class LoginForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    descricao = TextAreaField('Descrição', validators=[DataRequired()])
    latitude = DecimalField('Latitude', places=10, validators=[DataRequired(), NumberRange(min=-90.0, max=90.0)])
    longitude = DecimalField('Longitude', places=10, validators=[DataRequired(), NumberRange(min=-180.0, max=180.0)])
    submit = SubmitField('Cadastrar')