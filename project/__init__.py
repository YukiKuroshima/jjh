# project/__init__.py


import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


# instantiate the app
app = Flask(__name__)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# instantiate the db
db = SQLAlchemy(app)


# model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)

    def __init__(self, username):
        self.username = username

    def tojson(self):
        return {
            # 'id': self.id,
            'username': self.username
        }


# routes
@app.route('/ping', methods=['GET'])
def ping_pong():
    db.session.add(User('TestUser'))
    db.session.commit()

    user = User.query.filter_by(username='TestUser').first()

    return jsonify({
        'status': 'success',
        'message': 'pong!',
        'users': user.username
    })
