#!/usr/bin/env python
from PyQt5 import QtGui
from PyQt5.QtCore import QFile
from PyQt5.QtCore import QIODevice
from PyQt5.QtCore import QTextStream
from PyQt5.QtWidgets import QMainWindow
from loginapi.ui_window import Ui_Window
import time


class SimpleWebkit(QMainWindow, Ui_Window):
    def __init__(self, parent=None, qApplication=None, url=None):
        self.cookieStr = ''
        self.cookies = ''
        self.q_app = qApplication
        super(SimpleWebkit, self).__init__(parent)

        self.setupUi(self, url=url)
        self.webView.loadFinished.connect(self.finishLoading)

    # def on_webView_loadFinished(self):
    #     self.cookies = self.webView.page().networkAccessManager().cookieJar().allCookies()
    #     self.q_app.quit()

    def finishLoading(self):
        try:
            pass
        except Exception as e:
            print(e)
        finally:
            self.q_app.exit()
            pass
