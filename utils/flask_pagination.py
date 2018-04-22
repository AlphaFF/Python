#!/usr/bin/env python3
# coding=utf-8


from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from gevent import monkey
from gevent.pywsgi import WSGIServer

monkey.patch_all()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@10.1.1.30:3306/test'
app.config['SECRET_KEY'] = 'hard to guess ...'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)


class EntName(db.Model):
    __tablename__ = 'zhixingren_new_jiubao'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    pagination = EntName.query.order_by(EntName.id.asc()).paginate(page, 10, error_out=False)
    entnames = pagination.items
    # pages = pagination.pages
    return jsonify({
        'names': [entname.name for entname in entnames],
        'count': pagination.total
    })


if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 7070), app)
    http_server.serve_forever()
