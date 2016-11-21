#!/usr/bin/env python
from PyQt5 import QtGui
from PyQt5.QtCore import QFile
from PyQt5.QtCore import QIODevice
from PyQt5.QtCore import QTextStream
from PyQt5.QtWidgets import QMainWindow
from loginapi.ui_window import Ui_Window
import time


class SimpleWebkit(QMainWindow, Ui_Window):
    def __init__(self, parent=None, qApplication=None):
        self.cookieStr = ''
        self.cookies = ''
        self.q_app = qApplication

        super(SimpleWebkit, self).__init__(parent)

        url = 'https://passport.lagou.com/login/login.html'
        # url = 'https://login.taobao.com/member/login.jhtml'
        self.setupUi(self, url=url)
        self.webView.loadFinished.connect(self.finishLoading)

    # def on_webView_loadFinished(self):
    #     self.cookies = self.webView.page().networkAccessManager().cookieJar().allCookies()
    #     self.q_app.quit()

    def finishLoading(self):
        try:
            js_code = """
                        document.cookie
                       """
            self.cookieStr = self.webView.page().mainFrame().evaluateJavaScript(js_code)
            print('document_cookieStr: ' + self.cookieStr)

            self.cookies = self.webView.page().networkAccessManager().cookieJar().allCookies()
            cookie_str = ''
            for cc in self.cookies:
                cookie_str += (cc.name().data().decode() + '=' + cc.value().data().decode() + '; ')
            print('cookieObject: ' + cookie_str)

            self.getBarcodeStr()
        except Exception as e:
            print(e)
        finally:
            # self.q_app.exit()
            pass

    def getBarcodeStr(self):
        js_code = """
                    function getBase64Image(img) {
                        var canvas = document.createElement("canvas");
                        canvas.width = img.width;
                        canvas.height = img.height;

                        var ctx = canvas.getContext("2d");
                        ctx.drawImage(img, 0, 0, img.width, img.height);

                        var dataURL = canvas.toDataURL("image/png");
                        return dataURL
                    }
                    getBase64Image(document.getElementsByClassName("yzm")[0])
                   """
        barcode_str = self.webView.page().mainFrame().evaluateJavaScript(js_code)
        print(barcode_str)
