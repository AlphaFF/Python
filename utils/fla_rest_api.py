#!/usr/bin/env python3
# coding=utf-8

from flask import Flask,request
from flask_restful import Resource,Api,reqparse

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello':'world'}

todos = {'1':1,'2':2,'3':3}
class Todo(Resource):
    def get(self,todo_id):
        return {todo_id:todos[todo_id]}

    def post(self,todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id:todos[todo_id]}

    def put(self,todo_id):
        parser = reqparse.RequestParser()
        parser.add_argument('task')
        todos['task'] = 'task'
        return todos,201

api.add_resource(HelloWorld,'/api/')
api.add_resource(Todo,'/todo/<todo_id>')

if __name__ == '__main__':
    app.run(debug=True,port=5656)