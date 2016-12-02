#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author leo hao
# os windows 7
from functools import partial

from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
from PyQt5.QtCore import QFile
from PyQt5.QtCore import QIODevice
from PyQt5.QtCore import QTextStream
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWebKitWidgets
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWebKitWidgets import QWebView

TARGET_URLS = (
    'http://stackoverflow.com',
    'http://github.com',
    'http://bitbucket.org',
    'http://news.ycombinator.com',
    'http://slashdot.org',
    'http://www.reddit.com',
    'http://www.dzone.com',
    'http://www.ideone.com',
    'http://jsfiddle.net',
)


class Crawler(object):
    def __init__(self, app):
        self.app = app
        self.results = dict()
        self.browsers = dict()

    def _load_finished(self, browser_id, ok):
        print(ok, browser_id)
        web_view, _flag = self.browsers[browser_id]
        self.browsers[browser_id] = (web_view, True)

        frame = web_view.page().mainFrame()
        self.results[frame.url()] = frame.toHtml()

        web_view.loadFinished.disconnect()
        web_view.stop()

        if all([closed for bid, closed in self.browsers.values()]):
            print('all finished')
            self.app.quit()

    def start(self, urls):
        for browser_id, url in enumerate(urls):
            web_view = QWebView()

            loaded = partial(self._load_finished, browser_id)
            web_view.loadFinished.connect(loaded)
            web_view.load(QtCore.QUrl(url))
            self.browsers[browser_id] = (web_view, False)
            web_view.show()


if __name__ == '__main__':
    app = QApplication([])
    crawler = Crawler(app)
    crawler.start(TARGET_URLS)
    app.exec_()
    print('got:', crawler.results.keys())
