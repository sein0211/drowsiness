from flask import Flask, Blueprint, render_template, request
from werkzeug.utils import secure_filename
import os

bp = Blueprint('myPage', __name__, url_prefix='/myPage')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'C:\projects\drowsiness\image'

@bp.route('/')
def myPage2():
    return render_template('myPage.html')

@bp.route('/upload')
def upload_file():
    return render_template('myPage.html')

@bp.route('/uploader', methods=['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        return '파일이 성공적으로 업로드되었습니다.'

if __name__ == '__main__':
    bp.run(debug=True)