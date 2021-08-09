from pybo import db

class TimeTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    # user = db.relationship('User', backref=db.backref('time_table'))
    monClass = db.Column(db.String(200))
    tuesClass = db.Column(db.String(200))
    wedClass = db.Column(db.String(200))
    thursClass = db.Column(db.String(200))
    friClass = db.Column(db.String(200))
    satClass = db.Column(db.String(200))
    sunClass = db.Column(db.String(200))