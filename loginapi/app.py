#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author Leo Hao
# OS Windows 7
from flask import Flask
from flask import request

from loginapi.simpleWebkit import SimpleWebkit

app = Flask(__name__)


def log(func):
    def wrapper(*args, **kwargs):
        try:
            print('do_fuc')
            return func(*args, **kwargs)
        except Exception as e:
            print(e)

    return wrapper


@app.route('/lagouInit', methods=['GET'])
def lagou_init():
    doLagou_init()
    return '<h1>initDone</h1>'


@log
def doLagou_init():
    from PyQt5.QtWidgets import QApplication
    import sys
    q_app = QApplication(sys.argv)
    win = SimpleWebkit(qApplication=q_app)
    win.show()
    q_app.exec_()
    # sys.exec_it(webkit_app.exec_())
    # print(win.cookies)
    win.close()
    q_app.exit()


@app.route('/lagouLogin', methods=['POST'])
def lagouLogin():
    pass


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'


if __name__ == '__main__':
    app.run(port=5001)
