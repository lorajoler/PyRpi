#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 08:39:37 2017

@author: estudis
"""

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *

class Browser(QWidget):

    def __init__(self):
        super (Browser, self).__init__()

        self.webview = QWebView(self)
        self.webview.load("http://google.com")
        self.setGeometry(0, 0, 800, 600)

        self.menu_bar = QHBoxLayout()
        self.main_layout = QVBoxLayout()
        self.main_layout.1234
