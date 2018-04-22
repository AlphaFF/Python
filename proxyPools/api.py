#!/usr/bin/env python3
# coding=utf-8

from proxyPools.ipManager import ProxyManager

from flask import Flask,jsonify,request

app = Flask(__name__)

api_list = {
    'get':'get an usable proxy',
    'refresh':'refresh proxy pool',
    'get_all':'get all proxy from proxy pool',
    'delete?proxy=127.0.0.1:8080':'delete an unable proxy'
}

@app.route('/')
def index():
    return jsonify(api_list)

@app.route('/get/')
def get():
    proxy = ProxyManager().get()
    if proxy:
        return proxy
    else:
        return '返回出错'

@app.route('/get_all/')
def getAll():
    proxies = ProxyManager().getAll()
    if proxies:
        return jsonify(list(proxies))
    else:
        return '返回出错'

@app.route('/delete/',methods=['GET'])
def delete():
    proxy = request.args.get('proxy')
    ProxyManager().delete(proxy)
    return 'success'

@app.route('/get_status/')
def get_status():
    status = ProxyManager().get_status()
    return jsonify(status)

def run():
    app.run(host='0.0.0.0',port=5000)

if __name__ == '__main__':
    run()