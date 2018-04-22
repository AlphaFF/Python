#!/usr/bin/env python3
# coding=utf-8


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# 数据库和模型设置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1:3306/test'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class Joke(db.Model):
    __tablename__ = 'joke'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(2048))
    fav_num = db.Column(db.Integer)
    tags = db.Column(db.String(16))
    data_from = db.Column(db.String(64))
    publish_time = db.Column(db.Date())

    def __repr__(self):
        return self.content

@app.route('/')
def index():
    count = Joke.query.count()
    tmp_id = random.choice([i for i in range(1, count + 1)])
    print(tmp_id)
    joke = Joke.query.get_or_404(tmp_id)
    return joke.content