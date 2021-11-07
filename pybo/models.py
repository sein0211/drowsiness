from pybo import db


class User(db.Model):
    __table_name__='User'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(7), nullable=False, unique=True)
    nickname = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    d_time = db.Column(db.String(10), nullable=False, default="00:00:00")
