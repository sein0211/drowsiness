from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class UserLoginForm(FlaskForm):
    student_id = StringField('아이디', validators = [DataRequired(), Length(7)])
    password = StringField('비밀번호', validators = [DataRequired()])