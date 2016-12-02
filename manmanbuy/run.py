#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author Leo Hao
# OS Windows 7
import re
from flask import Flask
from flask import request
from PyQt5.QtWidgets import QApplication
import sys
from simpleWebkit import SimpleWebkit
import time

app = Flask(__name__)


def log(func):
    def wrapper(*args, **kwargs):
        try:
            print('do_fuc')
            return func(*args, **kwargs)
        except Exception as e:
            print(e)

    return wrapper


# 中文--> gbk --> hex()
def get_chinese_gbk(old):
    new_str = ''
    if old is None or '' == old :
        return new_str

    for str in old:
        # print(str)
        not_chinese_str = re.search("[a-zA-Z0-9]", str)
        if not_chinese_str:
            new_str += not_chinese_str.group(0)
            continue

        if str == " ":
            new_str += "+"
            continue

        str_bytes = str.encode('gbk')
        for b in str_bytes:
            new_str += hex(b).replace('0x', '%')

    return new_str


@app.route('/ManmanbuySearch', methods=['GET'])
def lagou_init():
    search_param = request.args.get("search_param")
    search_param = get_chinese_gbk(search_param)
    # print(search_param)
    do_search(search_param)
    return 'SearchDone'


q_app = QApplication(sys.argv)


@log
def do_search(search_param):
    url = 'http://s.manmanbuy.com/Default.aspx?key=' + search_param
    win = SimpleWebkit(qApplication=q_app, url=url)
    win.show()
    q_app.exec_()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
