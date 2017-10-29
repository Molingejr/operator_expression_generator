# FileName: browser.py
"""
This module is responsible for displaying the user manual on a browser.
It contains classes responsible for managing and displaying the browser.
"""

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget 
from PyQt5.QtWebKitWidgets import QWebView, QWebPage  # This module has been deprecated
from PyQt5.QtWebKit import QWebSettings     # This module has been deprecated
from PyQt5.QtNetwork import *
import sys
import os
from optparse import OptionParser
 
 
class MyBrowser(QWebPage):
    """ Settings for the browser."""
 
    def userAgentForUrl(self, url):
        """ Returns a User Agent that will be seen by the website. """
        return "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"


class Browser(QWebView):
    """
    Controls and run the browser.
    """
    def __init__(self):
        # QWebView
        self.view = QWebView.__init__(self)
        # self.view.setPage(MyBrowser())
        self.setWindowTitle('Loading...')
        self.titleChanged.connect(self.adjustTitle)
        # super(Browser).connect(self.ui.webView, QtCore.SIGNAL("titleChanged (const QString&)"), self.adjustTitle)
 
    def load(self, url):
        self.setUrl(QUrl(url))
 
    def adjustTitle(self):
        self.setWindowTitle(self.title())
 
    def disableJS(self):
        settings = QWebSettings.globalSettings()
        settings.setAttribute(QWebSettings.JavascriptEnabled, False)


if __name__ == '__main__':
    os.chdir('help')    # change current directory to the help directory

    app = QApplication(sys.argv)
    view = Browser()
    view.showMaximized()
    view.load("file://{}/UserManual.html".format(os.getcwd()))   # load index.html at help directory
    app.exec_()
