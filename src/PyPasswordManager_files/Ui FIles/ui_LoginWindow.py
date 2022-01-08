# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginWindowHESLty.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(445, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginWindow.sizePolicy().hasHeightForWidth())
        LoginWindow.setSizePolicy(sizePolicy)
        LoginWindow.setMinimumSize(QSize(445, 400))
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 120, 391, 231))
        self.mainLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.aUsernameLayout = QHBoxLayout()
        self.aUsernameLayout.setObjectName(u"aUsernameLayout")
        self.usernameLabel = QLabel(self.verticalLayoutWidget)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.aUsernameLayout.addWidget(self.usernameLabel)

        self.usernameEntry = QLineEdit(self.verticalLayoutWidget)
        self.usernameEntry.setObjectName(u"usernameEntry")

        self.aUsernameLayout.addWidget(self.usernameEntry)


        self.mainLayout.addLayout(self.aUsernameLayout)

        self.bPasswordLayout = QHBoxLayout()
        self.bPasswordLayout.setObjectName(u"bPasswordLayout")
        self.passwordLabel = QLabel(self.verticalLayoutWidget)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.bPasswordLayout.addWidget(self.passwordLabel)

        self.passwordEntry = QLineEdit(self.verticalLayoutWidget)
        self.passwordEntry.setObjectName(u"passwordEntry")

        self.bPasswordLayout.addWidget(self.passwordEntry)

        self.showPasswordButton = QPushButton(self.verticalLayoutWidget)
        self.showPasswordButton.setObjectName(u"showPasswordButton")

        self.bPasswordLayout.addWidget(self.showPasswordButton)


        self.mainLayout.addLayout(self.bPasswordLayout)

        self.loginButtonLayout = QHBoxLayout()
        self.loginButtonLayout.setObjectName(u"loginButtonLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.loginButtonLayout.addItem(self.horizontalSpacer_2)

        self.rememberLogin = QPushButton(self.verticalLayoutWidget)
        self.rememberLogin.setObjectName(u"rememberLogin")

        self.loginButtonLayout.addWidget(self.rememberLogin)

        self.loginButton = QPushButton(self.verticalLayoutWidget)
        self.loginButton.setObjectName(u"loginButton")

        self.loginButtonLayout.addWidget(self.loginButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.loginButtonLayout.addItem(self.horizontalSpacer)


        self.mainLayout.addLayout(self.loginButtonLayout)

        self.signupLayout = QHBoxLayout()
        self.signupLayout.setObjectName(u"signupLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.signupLayout.addItem(self.horizontalSpacer_3)

        self.signupButton = QPushButton(self.verticalLayoutWidget)
        self.signupButton.setObjectName(u"signupButton")

        self.signupLayout.addWidget(self.signupButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.signupLayout.addItem(self.horizontalSpacer_4)


        self.mainLayout.addLayout(self.signupLayout)

        self.LoginLabel = QLabel(self.centralwidget)
        self.LoginLabel.setObjectName(u"LoginLabel")
        self.LoginLabel.setGeometry(QRect(180, 20, 111, 68))
        font = QFont()
        font.setPointSize(30)
        self.LoginLabel.setFont(font)
        LoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(LoginWindow)
        self.statusbar.setObjectName(u"statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"MainWindow", None))
        self.usernameLabel.setText(QCoreApplication.translate("LoginWindow", u"Username: ", None))
        self.passwordLabel.setText(QCoreApplication.translate("LoginWindow", u"Password: ", None))
        self.showPasswordButton.setText(QCoreApplication.translate("LoginWindow", u"Show", None))
        self.rememberLogin.setText(QCoreApplication.translate("LoginWindow", u"Remember and Login", None))
        self.loginButton.setText(QCoreApplication.translate("LoginWindow", u"Login", None))
        self.signupButton.setText(QCoreApplication.translate("LoginWindow", u"Signup", None))
        self.LoginLabel.setText(QCoreApplication.translate("LoginWindow", u"Login", None))
    # retranslateUi

