from flask import Blueprint
from flask import render_template
import cv2

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    return render_template('main.html')
    # 나중에 회원의 '닉네임'값을 넘겨줘야함. 그래야 출력해줄 수 있음



