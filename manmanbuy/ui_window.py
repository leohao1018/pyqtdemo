# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Fri Jul 26 06:50:59 2013
#      by: PyQt5 UI code generator 5.0.1-snapshot-2a99e59669ee
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWebKitWidgets
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWebKitWidgets import QWebView


class Ui_Window(object):
    def setupUi(self, Window, url=''):
        Window.setObjectName("Window")
        Window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(-1, 4, -1, 4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # self.webView = QtWebKitWidgets.QWebView(self.centralwidget)
        # self.webView.setUrl(QtCore.QUrl(url))
        # self.webView.setObjectName("webView")

        self.webView = QWebView(self)
        self.webView.setUrl(QtCore.QUrl(url))
        self.webView.setObjectName("webView")
        self.verticalLayout_2.addWidget(self.webView)
        Window.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(Window)



