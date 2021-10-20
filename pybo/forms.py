from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo


class UserLoginForm(FlaskForm):
    student_id = StringField('학번', validators=[DataRequired(), Length(7)])
    password = StringField('비밀번호', validators=[DataRequired()])


class UserCreateForm(FlaskForm):
    student_id = StringField('학번', validators=[DataRequired(), Length(min=7, max=7)])
    nickname = StringField('닉네임', validators=[DataRequired(), Length(min=3, max=20)])
    # DataRequired(): 필수 항목 지정 / Length(min=3, max=20): 길이 조건
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    # password1과 password2는 일치해야 하므로 EqualTo 검증 추가
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
