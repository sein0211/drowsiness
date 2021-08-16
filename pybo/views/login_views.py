from flask import Blueprint, render_template

from pybo.models import User

bp = Blueprint('login', __name__, url_prefix='/login')


@bp.route('/')
def login():
    return render_template('login/login.html')
