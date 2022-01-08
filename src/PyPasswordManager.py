#! /usr/bin/python3
# -*- coding: utf-8 -*-
################## THE IMPORTS ######################################################
from PyQt5 import QtCore, QtGui, QtWidgets
from difflib import get_close_matches
from datetime import datetime as dt
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import sys
import os
import glob
import shelve
import random
import string
import time
import sqlite3 as sq
import pyperclip as ppc
import base64

#################### IMPORTS END HERE ###########################

#################################################################
################# MAIN WINDOW UI AND BACKEND ####################
#################################################################
class Ui_PasswordManager(object):
	def setupUi(self, PasswordManager):
		self.mainManager = PasswordManager
		PasswordManager.setObjectName("PasswordManager")
		PasswordManager.resize(699, 445)
		icon = QtGui.QIcon()
		icon.addFile("main.ico", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		PasswordManager.setWindowIcon(icon)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(PasswordManager.sizePolicy().hasHeightForWidth())
		PasswordManager.setSizePolicy(sizePolicy)
		PasswordManager.setMinimumSize(QtCore.QSize(699, 445))
		PasswordManager.setMaximumSize(QtCore.QSize(699, 445))
		PasswordManager.setBaseSize(QtCore.QSize(699, 445))
		self.centralwidget = QtWidgets.QWidget(PasswordManager)
		self.centralwidget.setObjectName("centralwidget")
		self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox.setGeometry(QtCore.QRect(300, 10, 381, 381))
		self.groupBox.setObjectName("groupBox")
		self.layoutWidget = QtWidgets.QWidget(self.groupBox)
		self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 361, 341))
		self.layoutWidget.setObjectName("layoutWidget")
		self.mainLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
		self.mainLayout.setContentsMargins(0, 0, 0, 0)
		self.mainLayout.setObjectName("mainLayout")
		self.urlLabel = QtWidgets.QLabel(self.layoutWidget)
		self.urlLabel.setObjectName("urlLabel")
		self.mainLayout.addWidget(self.urlLabel)
		self.aNameLayout = QtWidgets.QHBoxLayout()
		self.aNameLayout.setObjectName("aNameLayout")
		self.nameEntry = QtWidgets.QLineEdit(self.layoutWidget)
		self.nameEntry.setObjectName("nameEntry")
		self.nameIcon = QtWidgets.QLabel(self.layoutWidget)
		self.aNameLayout.addWidget(self.nameEntry)
		self.aNameLayout.addWidget(self.nameIcon)
		self.mainLayout.addLayout(self.aNameLayout)
		self.websiteLabel = QtWidgets.QLabel(self.layoutWidget)
		self.websiteLabel.setObjectName("websiteLabel")
		self.mainLayout.addWidget(self.websiteLabel)
		self.bUrlLayout = QtWidgets.QHBoxLayout()
		self.bUrlLayout.setObjectName("bUrlLayout")
		self.urlEntry = QtWidgets.QLineEdit(self.layoutWidget)
		self.urlEntry.setObjectName("urlEntry")
		self.bUrlLayout.addWidget(self.urlEntry)
		self.urlCopyButton = QtWidgets.QPushButton(self.layoutWidget)
		self.urlCopyButton.setMinimumSize(QtCore.QSize(84, 26))
		self.urlCopyButton.setObjectName("urlCopyButton")
		self.bUrlLayout.addWidget(self.urlCopyButton)
		self.urlPasteButton = QtWidgets.QPushButton(self.layoutWidget)
		self.urlPasteButton.setObjectName("urlPasteButton")
		self.bUrlLayout.addWidget(self.urlPasteButton)
		self.mainLayout.addLayout(self.bUrlLayout)
		self.emailLabel = QtWidgets.QLabel(self.layoutWidget)
		self.emailLabel.setObjectName("emailLabel")
		self.mainLayout.addWidget(self.emailLabel)
		self.cEmailLayout = QtWidgets.QHBoxLayout()
		self.cEmailLayout.setObjectName("cEmailLayout")
		self.emailEntry = QtWidgets.QLineEdit(self.layoutWidget)
		self.emailEntry.setObjectName("emailEntry")
		self.cEmailLayout.addWidget(self.emailEntry)
		self.emailCopyButton = QtWidgets.QPushButton(self.layoutWidget)
		self.emailCopyButton.setObjectName("emailCopyButton")
		self.cEmailLayout.addWidget(self.emailCopyButton)
		self.emailPasteButton = QtWidgets.QPushButton(self.layoutWidget)
		self.emailPasteButton.setObjectName("emailPasteButton")
		self.cEmailLayout.addWidget(self.emailPasteButton)
		self.mainLayout.addLayout(self.cEmailLayout)
		self.passwordLabel = QtWidgets.QLabel(self.layoutWidget)
		self.passwordLabel.setObjectName("passwordLabel")
		self.mainLayout.addWidget(self.passwordLabel)
		self.dPasswordLayout = QtWidgets.QHBoxLayout()
		self.dPasswordLayout.setObjectName("dPasswordLayout")
		self.passwordEntry = QtWidgets.QLineEdit(self.layoutWidget)
		self.passwordEntry.setObjectName("passwordEntry")
		self.dPasswordLayout.addWidget(self.passwordEntry)
		self.passwordCopyButton = QtWidgets.QPushButton(self.layoutWidget)
		self.passwordCopyButton.setObjectName("passwordCopyButton")
		self.dPasswordLayout.addWidget(self.passwordCopyButton)
		self.passwordPasteButton = QtWidgets.QPushButton(self.layoutWidget)
		self.passwordPasteButton.setObjectName("passwordPasteButton")
		self.dPasswordLayout.addWidget(self.passwordPasteButton)
		self.mainLayout.addLayout(self.dPasswordLayout)
		self.passwordShowBox = QtWidgets.QCheckBox(self.layoutWidget)
		self.passwordShowBox.setObjectName("passwordShowBox")
		self.mainLayout.addWidget(self.passwordShowBox)
		self.notesLabel = QtWidgets.QLabel(self.layoutWidget)
		self.notesLabel.setObjectName("notesLabel")
		self.mainLayout.addWidget(self.notesLabel)
		self.notesEntry = QtWidgets.QTextEdit(self.layoutWidget)
		self.notesEntry.setObjectName("notesEntry")
		self.mainLayout.addWidget(self.notesEntry)
		self.buttonLayout = QtWidgets.QHBoxLayout()
		self.buttonLayout.setObjectName("buttonLayout")
		self.addButton = QtWidgets.QPushButton(self.layoutWidget)
		self.addButton.setObjectName("addButton")
		self.buttonLayout.addWidget(self.addButton)
		self.editButton = QtWidgets.QPushButton(self.layoutWidget)
		self.editButton.setObjectName("editButton")
		self.buttonLayout.addWidget(self.editButton)
		self.deleteButton = QtWidgets.QPushButton(self.layoutWidget)
		self.deleteButton.setObjectName("deleteButton")
		self.buttonLayout.addWidget(self.deleteButton)
		self.mainLayout.addLayout(self.buttonLayout)
		self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 271, 361))
		self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
		self.listLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
		self.listLayout.setContentsMargins(0, 0, 0, 0)
		self.listLayout.setObjectName("listLayout")
		self.searchEntry = QtWidgets.QLineEdit(self.verticalLayoutWidget)
		self.searchEntry.setObjectName("searchEntry")
		self.listLayout.addWidget(self.searchEntry)
		self.mainList = QtWidgets.QListWidget(self.verticalLayoutWidget)
		self.mainList.setObjectName("mainList")
		self.listLayout.addWidget(self.mainList)
		self.buttonLayoutRefresh = QtWidgets.QHBoxLayout()
		self.buttonLayoutRefresh.setObjectName("buttonLayoutRefresh")
		spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.buttonLayoutRefresh.addItem(spacerItem)
		self.clearButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.clearButton.setObjectName("clearButton")
		self.buttonLayoutRefresh.addWidget(self.clearButton)
		spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.buttonLayoutRefresh.addItem(spacerItem1)
		self.listLayout.addLayout(self.buttonLayoutRefresh)
		PasswordManager.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(PasswordManager)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 699, 32))
		self.menubar.setObjectName("menubar")
		self.menuFile = QtWidgets.QMenu(self.menubar)
		self.menuFile.setObjectName("menuFile")
		self.menuHelp = QtWidgets.QMenu(self.menubar)
		self.menuHelp.setObjectName("menuHelp")
		self.menuTools = QtWidgets.QMenu(self.menubar)
		self.menuTools.setObjectName("menuTools")
		PasswordManager.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(PasswordManager)
		self.statusbar.setObjectName("statusbar")
		PasswordManager.setStatusBar(self.statusbar)
		self.actionExit = QtWidgets.QAction(PasswordManager)
		self.actionExit.setObjectName("actionExit")
		self.actionAbout = QtWidgets.QAction(PasswordManager)
		self.actionAbout.setObjectName("actionAbout")
		self.actionPasswordGenerator = QtWidgets.QAction(PasswordManager)
		self.actionPasswordGenerator.setObjectName("actionPasswordGenerator")
		self.actionImport = QtWidgets.QAction(PasswordManager)
		self.actionImport.setObjectName("actionImport")
		self.actionExport = QtWidgets.QAction(PasswordManager)
		self.actionExport.setObjectName("actionExport")
		self.actionRefresh = QtWidgets.QAction(PasswordManager)
		self.actionRefresh.setObjectName("actionRefresh")
		self.menuFile.addSeparator()
		self.menuFile.addAction(self.actionExit)
		self.menuHelp.addAction(self.actionAbout)
		self.menuTools.addAction(self.actionPasswordGenerator)
		self.menuTools.addSeparator()
		self.menuTools.addAction(self.actionImport)
		self.menuTools.addAction(self.actionExport)
		self.menuTools.addSeparator()
		self.menuTools.addAction(self.actionRefresh)
		self.menubar.addAction(self.menuFile.menuAction())
		self.menubar.addAction(self.menuTools.menuAction())
		self.menubar.addAction(self.menuHelp.menuAction())

		self.retranslateUi(PasswordManager)
		QtCore.QMetaObject.connectSlotsByName(PasswordManager)

	def retranslateUi(self, PasswordManager):
		_translate = QtCore.QCoreApplication.translate
		self.retranslate = _translate
		PasswordManager.setWindowTitle(_translate("PasswordManager", "PasswordManager"))
		self.urlLabel.setText(_translate("PasswordManager", "Name"))
		self.websiteLabel.setText(_translate("PasswordManager", "Url"))
		self.urlCopyButton.setText(_translate("PasswordManager", "Copy"))
		self.urlPasteButton.setText(_translate("PasswordManager", "Paste"))
		self.emailLabel.setText(_translate("PasswordManager", "Email"))
		self.emailCopyButton.setText(_translate("PasswordManager", "Copy"))
		self.emailPasteButton.setText(_translate("PasswordManager", "Paste"))
		self.passwordLabel.setText(_translate("PasswordManager", "Password"))
		self.passwordCopyButton.setText(_translate("PasswordManager", "Copy"))
		self.passwordPasteButton.setText(_translate("PasswordManager", "Paste"))
		self.passwordShowBox.setText(_translate("PasswordManager", "Show Password"))
		self.notesLabel.setText(_translate("PasswordManager", "Notes"))
		self.addButton.setText(_translate("PasswordManager", "Add"))
		self.editButton.setText(_translate("PasswordManager", "Edit"))
		self.deleteButton.setText(_translate("PasswordManager", "Delete"))
		self.searchEntry.setPlaceholderText(_translate("PasswordManager", "Search"))

		self.clearButton.setText(_translate("PasswordManager", "Clear"))
		self.menuFile.setTitle(_translate("PasswordManager", "File"))
		self.menuHelp.setTitle(_translate("PasswordManager", "Help"))
		self.menuTools.setTitle(_translate("PasswordManager", "Tools"))
		self.actionExit.setText(_translate("PasswordManager", "Logout and Exit"))
		self.actionExit.setStatusTip(_translate("PasswordManager", "Logout and Exit, Such Simple"))
		self.actionExit.setShortcut(_translate("PasswordManager", "Ctrl+Q"))
		self.actionAbout.setText(_translate("PasswordManager", "About"))
		self.actionAbout.setStatusTip(_translate("PasswordManager", "About the Program"))
		self.actionAbout.setShortcut(_translate("PasswordManager", "F1"))
		self.actionPasswordGenerator.setText(_translate("PasswordManager", "Password Generator"))
		self.actionPasswordGenerator.setStatusTip(_translate("PasswordManager", "Generate Password"))
		self.actionPasswordGenerator.setShortcut(_translate("PasswordManager", "Ctrl+G"))
		self.actionImport.setText(_translate("PasswordManager", "Import"))
		self.actionImport.setStatusTip(_translate("PasswordManager", "Import From a Previous Backup"))
		self.actionImport.setShortcut(_translate("PasswordManager", "Ctrl+I"))
		self.actionExport.setText(_translate("PasswordManager", "Export"))
		self.actionExport.setStatusTip(_translate("PasswordManager", "Export To A New Backup File"))
		self.actionExport.setShortcut(_translate("PasswordManager", "Ctrl+E"))
		self.actionRefresh.setText(_translate("PasswordManager", "Refresh List"))
		self.actionRefresh.setStatusTip(_translate("PasswordManager", "If By Some Reason The List Doesn't Refresh"))
		self.actionRefresh.setShortcut(_translate("PasswordManager", "Ctrl+R"))

		self.actionAbout.triggered.connect(lambda : (QtWidgets.QMessageBox.about(PasswordManager, 'About PyPasswordManager', 'This Useless "PyPasswordManager", was Created By Yeager\nFind him at his Discord at Yeager#1902\nAt his Server discord.gg/Z6wrbYs\nSay something Offensive To Him')))

class PasswordManager(QtWidgets.QMainWindow, Ui_PasswordManager):
	def __init__(self, username, password, parent = None):
		self.backend = PyPasswordManagerBack(username, password)
		QtWidgets.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.username = username
		self.password = password
		self.groupBox.setTitle(f"Welcome {self.username}")
		self.ui_finalization()
		self.refresh_list()
	
	def ui_finalization(self):
		self.passwordEntry.setEchoMode(QtWidgets.QLineEdit.Password)
		self.passwordShowBox.stateChanged.connect(self.password_view)
		self.mainList.itemClicked.connect(self.view_password)
		self.urlCopyButton.clicked.connect(lambda : (ppc.copy(self.urlEntry.text())))
		self.emailCopyButton.clicked.connect(lambda : (ppc.copy(self.emailEntry.text())))
		self.passwordCopyButton.clicked.connect(lambda : (ppc.copy(self.passwordEntry.text())))
		self.urlPasteButton.clicked.connect(lambda : (self.urlEntry.setText(ppc.paste())))
		self.emailPasteButton.clicked.connect(lambda : (self.emailEntry.setText(ppc.paste())))
		self.passwordPasteButton.clicked.connect(lambda : (self.passwordEntry.setText(ppc.paste())))
		self.addButton.clicked.connect(self.add_button)
		self.editButton.clicked.connect(self.edit_button)
		self.deleteButton.clicked.connect(self.delete_button)
		self.clearButton.clicked.connect(self.clear_button)
		self.actionPasswordGenerator.triggered.connect(self.generate_password)
		self.searchEntry.textChanged.connect(self.search_function)
		self.actionImport.triggered.connect(self.import_passwords)
		self.actionExport.triggered.connect(self.export_passwords)
		self.actionExit.triggered.connect(self.logout_exit)

	
	def logout_exit(self):
		if os.path.exists(os.path.join('.', 'PyPasswordManager_files', "remember")):
			os.remove(os.path.join('.', 'PyPasswordManager_files', "remember"))
		sys.exit(0)

	def password_view(self, state):
		if state == QtCore.Qt.Checked:
			self.passwordEntry.setEchoMode(QtWidgets.QLineEdit.Normal)
		else:
			self.passwordEntry.setEchoMode(QtWidgets.QLineEdit.Password)

	# TO REPLACE
	def refresh_list(self):
		self.mainList.clear()
		__sortingEnabled = self.mainList.isSortingEnabled()
		self.mainList.setSortingEnabled(False)
		saved = self.backend.refresh_list()
		if not saved == None:
			for i in range(0,len(saved)):
				item = QtWidgets.QListWidgetItem()
				if item == None:
					continue
				item.setText(self.retranslate("self.mainManager", f"{saved[i]}"))
				if not self.view_icon(saved[i]) == None:
					item.setIcon(QtGui.QIcon(self.view_icon(saved[i])))
				self.mainList.setIconSize(QtCore.QSize(25, 25))
				self.mainList.addItem(item)
		self.mainList.setSortingEnabled(__sortingEnabled)

	
	def view_password(self, signal):
		self.currentSelected = self.mainList.item(self.mainList.row(signal)).text()
		saved = self.backend.view_entry(self.currentSelected)
		if not saved == None:
			self.nameEntry.setText(saved["name"])
			pixIcon = QtGui.QPixmap(self.view_icon(saved["name"]))
			scaledIcon = pixIcon.scaled(25,25)
			self.nameIcon.setPixmap(scaledIcon)
			self.urlEntry.setText(saved["url"])
			self.emailEntry.setText(saved["email"])
			self.passwordEntry.setText(saved["password"])
			self.notesEntry.setPlainText(saved["notes"])

		else:
			QtWidgets.QMessageBox.critical(self.mainManager, "Can't View Password", "There seems to be a Problem")
	
	def add_button(self):
		info = {"name": f"{self.nameEntry.text()}",
				"url": f"{self.urlEntry.text()}", 
				"email": f"{self.emailEntry.text()}",
				"password": f"{self.passwordEntry.text()}", 
				"notes": f"{self.notesEntry.toPlainText()}"
			   }
		if self.urlEntry.text() != "" and self.emailEntry.text() != '' and self.passwordEntry.text() != '' and self.nameEntry.text() != '':
			if not self.backend.add_entry(self.nameEntry.text(), info):
				QtWidgets.QMessageBox.critical(self.mainManager, "Failure", "Entry Couldn't Be Added\nIt Already Exists, Choose A Different Name")
		else:
			QtWidgets.QMessageBox.warning(self.mainManager, "Failure", "Can't Add Empty Strings")
		self.refresh_list()

	
	def delete_button(self):
		if not self.backend.remove_entry(self.currentSelected):
			QtWidgets.QMessageBox.critical(self.mainManager, 'Failure', "For Some Reason, Entry Couldn't Be Deleted")
		self.refresh_list()
		self.clear_button()

	
	def edit_button(self):
		info = {"name": f"{self.nameEntry.text()}",
				"url": f"{self.urlEntry.text()}", 
				"email": f"{self.emailEntry.text()}",
				"password": f"{self.passwordEntry.text()}", 
				"notes": f"{self.notesEntry.toPlainText()}"
			   }
		if self.backend.edit_entry(self.currentSelected, self.nameEntry.text(), info):
			QtWidgets.QMessageBox.information(self.mainManager, 'Success', "Entry Edit Successful")
		else:
			QtWidgets.QMessageBox.critical(self.mainManager, 'Failure', "For Some Reason, Entry Couldn't Be edit")
		self.refresh_list()

	# END TO REPLACE
	def clear_button(self):
		self.nameEntry.clear()
		self.urlEntry.clear()
		self.emailEntry.clear()
		self.passwordEntry.clear()
		self.notesEntry.clear()
		self.nameIcon.clear()

	
	def search_function(self, key):
		self.mainList.clear()
		__sortingEnabled = self.mainList.isSortingEnabled()
		self.mainList.setSortingEnabled(False)
		saved = self.backend.refresh_list()
		if not saved == None:
			for itemKey in saved:
				if itemKey.lower().__contains__(key.lower()):
					item = QtWidgets.QListWidgetItem()
					if item == None:
						continue
					item.setText(self.retranslate("self.mainManager", f"{itemKey}"))
					item.setIcon(QtGui.QIcon(self.view_icon(itemKey)))
					self.mainList.setIconSize(QtCore.QSize(25, 25))
					self.mainList.addItem(item)

	
	def generate_password(self):
		genPass = PasswordGenerator_Ui(self.mainManager)
		genPass.show()
	
	def view_icon(self, ico):
		if os.path.exists(os.path.join("PyPasswordManager_files", "icons")):
			iconList = glob.glob(os.path.join("PyPasswordManager_files", "icons", "*.png"))
			iconDict = {"Blank": "Blank"}
			for i in range(len(iconList)):
				iconDict.__setitem__(iconList[i].split("/")[-1].split(".")[0], iconList[i])
			try:
				for i in range(len(ico.split(" "))):
					webpage = get_close_matches(ico.lower(), iconDict.keys())[0]
					if webpage in iconDict.keys():
						return iconDict[webpage]
					else:
						return None
			except:
				try:
					if get_close_matches(ico.lower(), iconDict.keys())[0] != None:
						return iconDict[get_close_matches(ico.lower(), iconDict.keys())[0]]
				except:
					return iconDict["delicious"]
		else:
			return None

	
	def export_passwords(self):
		expui = ExportDialog_Ui(self.username, self.password, self.mainManager)
		expui.show()

	
	def import_passwords(self):
		impui = ImportDialog_Ui(self.username, self.password, self.mainManager)
		impui.show()
		self.update()


############ BACKEND ###############
class PyPasswordManagerBack():	
	def __init__(self, username, password):
		self.fileFolder = os.path.join(".", "PyPasswordManager_files")
		os.makedirs(self.fileFolder, exist_ok = True)
		self.username = username
		self.password = password
		self.crypt = Encryption()
		self.userFile = os.path.join(".", "PyPasswordManager_files", f"{self.username}_passwords")

	
	def check_existing(self):
		try:
			with shelve.open(self.userFile) as shfile:
				if len(list(shfile.keys())) == 0:
					return False
				else:
					return True


		except:
			return False

	
	def view_entry(self, i):
		if self.check_existing() and i != None:
			with shelve.open(self.userFile) as shfile:
				saved = dict(shfile)
				newSaved = saved[i]
				newSaved["email"] = str(self.crypt.decrypt_string(saved[i]["email"], self.password)).removeprefix("b'")
				newSaved["email"] = newSaved["email"].removesuffix("'")
				newSaved["password"] = str(self.crypt.decrypt_string(saved[i]["password"], self.password)).removeprefix("b'")
				newSaved["password"] = newSaved["password"].removesuffix("'")
				return newSaved

		else:
			return None

	
	def refresh_list(self):
		if self.check_existing():
			with shelve.open(self.userFile) as shfile:
				saved = list(shfile.keys())
				return saved


		else:
			return None
	
	def add_entry(self, key, addict):
		addict["email"] = str(self.crypt.encrypt_string(addict["email"], self.password))
		addict["password"] = str(self.crypt.encrypt_string(addict["password"], self.password))
		with shelve.open(self.userFile) as shfile:
			if key in list(shfile.keys()) and not key in ["", None]:
				return False
			else:
				shfile[key] = addict
				return True

	
	def remove_entry(self, key):
		try:
			with shelve.open(self.userFile) as shfile:
				del shfile[key]
				return True

		except:
			return False

	
	def edit_entry(self, key, newkey, eddict):
		eddict["email"] = str(self.crypt.encrypt_string(eddict["email"], self.password))
		eddict["password"] = str(self.crypt.encrypt_string(eddict["password"], self.password))
		try:
			with shelve.open(self.userFile) as shfile:
				del shfile[key]
				shfile[newkey] = eddict
			return True
		except:
			return False


#################################################################
################# LOGIN WINDOW AND IT'S BACKEND #################
#################################################################
class Ui_LoginWindow(object):
	def setupUi(self, LoginWindow):
		self.mainLoginWindow = LoginWindow
		if not LoginWindow.objectName():
			LoginWindow.setObjectName(u"LoginWindow")
		LoginWindow.resize(445, 400)
		icon = QtGui.QIcon()
		icon.addFile("main.ico", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		LoginWindow.setWindowIcon(icon)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(LoginWindow.sizePolicy().hasHeightForWidth())
		LoginWindow.setSizePolicy(sizePolicy)
		LoginWindow.setMinimumSize(QtCore.QSize(445, 400))
		self.centralwidget = QtWidgets.QWidget(LoginWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 120, 391, 231))
		self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
		self.mainLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
		self.mainLayout.setContentsMargins(0, 0, 0, 0)
		self.mainLayout.setObjectName("mainLayout")
		self.aUsernameLayout = QtWidgets.QHBoxLayout()
		self.aUsernameLayout.setObjectName("aUsernameLayout")
		self.usernameLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.usernameLabel.setObjectName("usernameLabel")
		self.aUsernameLayout.addWidget(self.usernameLabel)
		self.usernameEntry = QtWidgets.QLineEdit(self.verticalLayoutWidget)
		self.usernameEntry.setObjectName("usernameEntry")
		self.aUsernameLayout.addWidget(self.usernameEntry)
		self.mainLayout.addLayout(self.aUsernameLayout)
		self.bPasswordLayout = QtWidgets.QHBoxLayout()
		self.bPasswordLayout.setObjectName("bPasswordLayout")
		self.passwordLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.passwordLabel.setObjectName("passwordLabel")
		self.bPasswordLayout.addWidget(self.passwordLabel)
		self.passwordEntry = QtWidgets.QLineEdit(self.verticalLayoutWidget)
		self.passwordEntry.setObjectName("passwordEntry")
		self.bPasswordLayout.addWidget(self.passwordEntry)
		self.showPasswordButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.showPasswordButton.setObjectName(u"showPasswordButton")
		self.bPasswordLayout.addWidget(self.showPasswordButton)
		self.mainLayout.addLayout(self.bPasswordLayout)
		self.loginButtonLayout = QtWidgets.QHBoxLayout()
		self.loginButtonLayout.setObjectName("loginButtonLayout")
		spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.loginButtonLayout.addItem(spacerItem4)
		self.rememberLogin = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.rememberLogin.setObjectName(u"rememberLogin")
		self.loginButtonLayout.addWidget(self.rememberLogin)
		self.loginButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.loginButton.setObjectName("loginButton")
		self.loginButtonLayout.addWidget(self.loginButton)
		spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.loginButtonLayout.addItem(spacerItem5)
		self.mainLayout.addLayout(self.loginButtonLayout)
		self.signupLayout = QtWidgets.QHBoxLayout()
		self.signupLayout.setObjectName("signupLayout")
		spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.signupLayout.addItem(spacerItem6)
		self.signupButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.signupButton.setObjectName("signupButton")
		self.signupLayout.addWidget(self.signupButton)
		spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.signupLayout.addItem(spacerItem7)
		self.mainLayout.addLayout(self.signupLayout)
		self.LoginLabel = QtWidgets.QLabel(self.centralwidget)
		self.LoginLabel.setGeometry(QtCore.QRect(180, 20, 111, 68))
		font = QtGui.QFont()
		font.setPointSize(30)
		self.LoginLabel.setFont(font)
		self.LoginLabel.setObjectName("LoginLabel")
		LoginWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(LoginWindow)
		self.statusbar.setObjectName("statusbar")
		LoginWindow.setStatusBar(self.statusbar)

		self.retranslateUi(LoginWindow)
		QtCore.QMetaObject.connectSlotsByName(LoginWindow)

	def retranslateUi(self, LoginWindow):
		_translate = QtCore.QCoreApplication.translate
		LoginWindow.setWindowTitle(_translate("LoginWindow", "LoginWindow"))
		self.usernameLabel.setText(_translate("LoginWindow", "Username: "))
		self.passwordLabel.setText(_translate("LoginWindow", "Password: "))
		self.showPasswordButton.setText(_translate("LoginWindow", u"Show", None))
		self.rememberLogin.setText(_translate("LoginWindow", u"Remember and Login", None))
		self.loginButton.setText(_translate("LoginWindow", "Login"))
		self.signupButton.setText(_translate("LoginWindow", "Signup"))
		self.LoginLabel.setText(_translate("LoginWindow", "Login"))

	
class LoginWindow(QtWidgets.QMainWindow, Ui_LoginWindow):
	
	def __init__(self, parent = None):
		QtWidgets.QMainWindow.__init__(self, parent)
		self.loggedIn = False
		self.loginBack = LoginWindow_back()
		self.username = None
		self.password = None
		self.setupUi(self)
		if self.loginBack.check_rememberence():
			QtWidgets.QApplication.closeAllWindows()
		self.ui_confirm()

	def ui_confirm(self):
		self.passwordEntry.setEchoMode(QtWidgets.QLineEdit.Password)
		self.showPasswordButton.pressed.connect(lambda : (self.passwordEntry.setEchoMode(QtWidgets.QLineEdit.Normal)))
		self.showPasswordButton.released.connect(lambda : (self.passwordEntry.setEchoMode(QtWidgets.QLineEdit.Password)))
		self.rememberLogin.clicked.connect(self.remember_and_login)
		self.loginButton.clicked.connect(self.login)
		self.signupButton.clicked.connect(self.sign_up)
	
	def remember_and_login(self):
		self.loginBack.remember_password(self.usernameEntry.text(), self.passwordEntry.text())
		self.login()
	
	def login(self):
		if self.loginBack.verification(f"{self.usernameEntry.text()}", f"{self.passwordEntry.text()}"):
			self.loggedIn = True
			self.username = f"{self.usernameEntry.text()}"
			self.password = self.passwordEntry.text()
			QtWidgets.QApplication.closeAllWindows()
		else:
			QtWidgets.QMessageBox().critical(self.mainLoginWindow, "Login Failed", f"No Username: {self.usernameEntry.text()} Found,\nI suggest You Sign Up Using the Button Below")
	
	def sign_up(self):
		if self.usernameEntry.text() != "" and self.passwordEntry.text() != "":
			if self.loginBack.sign_up(f"{self.usernameEntry.text()}", f"{self.passwordEntry.text()}"):
				userExists = QtWidgets.QMessageBox().question(self.mainLoginWindow, "Sign Up Failed", f"Username {self.usernameEntry.text()} Exists,\nAre You Sure You are Not Forgetting the Password\nMake New User? (This is irreversible, and Will delete Data)", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
				if userExists == QtWidgets.QMessageBox.Yes:
					self.loginBack.sign_up_new(self.usernameEntry.text(), self.passwordEntry.text())
					QtWidgets.QMessageBox().information(self.mainLoginWindow, "Sign Up Successful", f"User {self.usernameEntry.text()} Signed Up Successful\nNow You May Login")
				else:
					QtWidgets.QMessageBox().critical(self.mainLoginWindow, "Sign up Failed", "For Some Reason We Couldn't Sign you Up\nContact Developer")
			else:
				QtWidgets.QMessageBox().information(self.mainLoginWindow, "Sign Up Successful", f"User {self.usernameEntry.text()} Signed Up Successful\nNow You May Login")
		else:
			QtWidgets.QMessageBox().critical(self.mainLoginWindow, "Ah, Such Empty", "It's Empty Drake!! The Username and Password Are Empty!")

############ BACKEND ###############
class LoginWindow_back():
	def __init__(self):
		self.fileFolder = os.path.join(".", "PyPasswordManager_files")
		os.makedirs(self.fileFolder, exist_ok=True)
		self.username = None
		self.file = os.path.join(f"{self.fileFolder}","LoginData")
		self.enc = "toremember"
		self.rememberpath = os.path.join(self.fileFolder, "remember")
		self.crypt = Encryption()
		self.check_rememberence()

	
	def verification(self, username, password):
		try:
			with shelve.open(self.file) as shfile:
				ver = shfile[f"{username}"]
				if ver["username"] == username and ver["password"] == password:
					self.username = username
					self.password = password
					return True
				else:
					return False


		except:
			return False

	
	def sign_up(self, username, password):
		with shelve.open(self.file) as shfile:
			if username in list(shfile.keys()):
				return True
			else:
				shfile[f"{username}"] = {"username": f"{username}", "password": f"{password}"}
				self.password = password
				return False


	
	def sign_up_new(self, username, password):
		with shelve.open(self.file) as shfile:
			shfile[f"{username}"] = {"username": f"{username}", "password": f"{password}"}
			self.password = password
			return True

	
	def remember_password(self, username, password):
		with shelve.open(self.rememberpath) as shfile:
			shfile[self.enc] = {
				"username": f"{str(self.crypt.encrypt_string(username, self.enc))}",
				"password": f"{str(self.crypt.encrypt_string(password, self.enc))}"
			}

	
	def check_rememberence(self):
		if os.path.exists(self.rememberpath):
			with shelve.open(self.rememberpath) as shfile:
				if len(list(shfile.keys())) == 0:
					return False
				else:
					userdict = shfile[self.enc]
					userdict["username"] = str(self.crypt.decrypt_string(userdict["username"], self.enc)).removeprefix("b'")
					userdict["username"] = userdict["username"].removesuffix("'")

					userdict["password"] = str(self.crypt.decrypt_string(userdict["password"], self.enc)).removeprefix("b'")
					userdict["password"] = userdict["password"].removesuffix("'")
					if self.verification(userdict["username"], userdict["password"]):
						return True
					else:
						return False
		else:
			return False

#################################################################
################# PASSWORD GENERATOR UI #########################
#################################################################
class Ui_PasswordGenerator(object):
	
	def setupUi(self, PasswordGenerator):
		PasswordGenerator.setObjectName("PasswordGenerator")
		PasswordGenerator.resize(503, 208)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(PasswordGenerator.sizePolicy().hasHeightForWidth())
		PasswordGenerator.setSizePolicy(sizePolicy)
		PasswordGenerator.setMinimumSize(QtCore.QSize(503, 208))
		PasswordGenerator.setMaximumSize(QtCore.QSize(503, 208))
		self.horizontalLayoutWidget_2 = QtWidgets.QWidget(PasswordGenerator)
		self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 100, 411, 31))
		self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
		self.generatedLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
		self.generatedLayout.setContentsMargins(0, 0, 0, 0)
		self.generatedLayout.setObjectName("generatedLayout")
		self.passwordGenerated = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
		self.passwordGenerated.setReadOnly(True)
		self.passwordGenerated.setObjectName("passwordGenerated")
		self.generatedLayout.addWidget(self.passwordGenerated)
		self.copyButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
		self.copyButton.setObjectName("copyButton")
		self.generatedLayout.addWidget(self.copyButton)
		self.horizontalLayoutWidget = QtWidgets.QWidget(PasswordGenerator)
		self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 60, 411, 31))
		self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
		self.generationLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
		self.generationLayout.setContentsMargins(0, 0, 0, 0)
		self.generationLayout.setObjectName("generationLayout")
		spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.generationLayout.addItem(spacerItem)
		self.numberSpin = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
		self.numberSpin.setObjectName("numberSpin")
		self.generationLayout.addWidget(self.numberSpin)
		spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.generationLayout.addItem(spacerItem1)
		self.generateButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		self.generateButton.setObjectName("generateButton")
		self.generationLayout.addWidget(self.generateButton)
		spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.generationLayout.addItem(spacerItem2)
		self.mainlabel = QtWidgets.QLabel(PasswordGenerator)
		self.mainlabel.setGeometry(QtCore.QRect(150, 10, 191, 21))
		font = QtGui.QFont()
		font.setPointSize(15)
		self.mainlabel.setFont(font)
		self.mainlabel.setObjectName("mainlabel")
		self.closeButton = QtWidgets.QPushButton(PasswordGenerator)
		self.closeButton.setGeometry(QtCore.QRect(210, 160, 84, 26))
		self.closeButton.setObjectName("closeButton")

		self.retranslateUi(PasswordGenerator)
		QtCore.QMetaObject.connectSlotsByName(PasswordGenerator)

	def retranslateUi(self, PasswordGenerator):
		_translate = QtCore.QCoreApplication.translate
		PasswordGenerator.setWindowTitle(_translate("PasswordGenerator", "Password Generator"))
		self.copyButton.setText(_translate("PasswordGenerator", "Copy"))
		self.generateButton.setText(_translate("PasswordGenerator", "Generate"))
		self.mainlabel.setText(_translate("PasswordGenerator", "Password Generator"))
		self.closeButton.setText(_translate("PasswordGenerator", "Close"))

		pass
	pass

class PasswordGenerator_Ui(QtWidgets.QDialog, Ui_PasswordGenerator):
	def __init__(self, parent = None):
		QtWidgets.QDialog.__init__(self, parent)
		self.setupUi(self)
		self.finalize_ui()
		
	def finalize_ui(self):
		self.numberSpin.setValue(15)
		self.generateButton.clicked.connect(self.generate)
		self.copyButton.setDisabled(True)
		self.copyButton.clicked.connect(lambda : (ppc.copy(self.passwordGenerated.text())))
		self.closeButton.clicked.connect(lambda : (self.close()))
		
	def generate(self):
		self.passwordGenerated.clear()
		num = self.numberSpin.value()
		custom = ''
		for n in range(num):
			x = random.randint(0, 94)
			custom += string.printable[x]
		self.passwordGenerated.setText(custom)
		self.copyButton.setEnabled(True)


#################################################################
################# IMPORTER DIALOG UI ############################
#################################################################
class Ui_ImportDialog(object):
	def setupUi(self, ImportDialog):
		self.ImportDialog = ImportDialog
		ImportDialog.setObjectName("ImportDialog")
		ImportDialog.resize(617, 250)
		ImportDialog.setMinimumSize(QtCore.QSize(617, 250))
		ImportDialog.setMaximumSize(QtCore.QSize(617, 250))
		ImportDialog.setStyleSheet("font: 10pt \"Cantarell\";")
		self.verticalLayoutWidget = QtWidgets.QWidget(ImportDialog)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 561, 191))
		self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
		self.mainLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
		self.mainLayout.setContentsMargins(0, 0, 0, 0)
		self.mainLayout.setObjectName("mainLayout")
		self.fileLayout = QtWidgets.QHBoxLayout()
		self.fileLayout.setObjectName("fileLayout")
		self.openLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.openLabel.setObjectName("openLabel")
		self.fileLayout.addWidget(self.openLabel)
		self.fileEntry = QtWidgets.QLineEdit(self.verticalLayoutWidget)
		self.fileEntry.setReadOnly(True)
		self.fileEntry.setObjectName("fileEntry")
		self.fileLayout.addWidget(self.fileEntry)
		self.browseButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.browseButton.setObjectName("browseButton")
		self.fileLayout.addWidget(self.browseButton)
		self.mainLayout.addLayout(self.fileLayout)
		self.passwordLayout = QtWidgets.QHBoxLayout()
		self.passwordLayout.setObjectName("passwordLayout")
		self.passwordLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.passwordLabel.setObjectName("passwordLabel")
		self.passwordLayout.addWidget(self.passwordLabel)
		self.passwordEntry = QtWidgets.QLineEdit(self.verticalLayoutWidget)
		self.passwordEntry.setEchoMode(QtWidgets.QLineEdit.Password)
		self.passwordEntry.setObjectName("passwordEntry")
		self.passwordLayout.addWidget(self.passwordEntry)
		self.mainLayout.addLayout(self.passwordLayout)
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem)
		self.importButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.importButton.setObjectName("importButton")
		self.horizontalLayout.addWidget(self.importButton)
		spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem1)
		self.mainLayout.addLayout(self.horizontalLayout)
		self.importProgress = QtWidgets.QProgressBar(self.verticalLayoutWidget)
		self.importProgress.setProperty("value", 0)
		self.importProgress.setInvertedAppearance(False)
		self.importProgress.setObjectName("importProgress")
		self.mainLayout.addWidget(self.importProgress)

		self.retranslateUi(ImportDialog)
		QtCore.QMetaObject.connectSlotsByName(ImportDialog)

	def retranslateUi(self, ImportDialog):
		_translate = QtCore.QCoreApplication.translate
		self._translate = _translate
		ImportDialog.setWindowTitle(_translate("ImportDialog", "Import Passwords"))
		self.openLabel.setText(_translate("ImportDialog", "Open File:"))
		self.browseButton.setText(_translate("ImportDialog", "Browse"))
		self.passwordLabel.setText(_translate("ImportDialog", "Password: "))
		self.passwordEntry.setPlaceholderText(_translate("ImportDialog", "Input Old Password"))
		self.importButton.setText(_translate("ImportDialog", "Import"))



class ImportDialog_Ui(QtWidgets.QDialog, Ui_ImportDialog):
	
	def __init__(self, username, password, parent = None):
		QtWidgets.QDialog.__init__(self, parent)
		self.setupUi(self)
		self.username = username
		self.password = password
		self.finalize_ui()
		self.options = QtWidgets.QFileDialog.Options()
		self.options = QtWidgets.QFileDialog.DontUseNativeDialog

	
	def finalize_ui(self):
		self.browseButton.clicked.connect(self.browse_db_file)
		self.importButton.clicked.connect(self.import_button)

	
	def browse_db_file(self):
		self.openfile, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", ".", "All Files (*);;Sqlite3 files (*.db, *.sqlite3)", options = self.options)
		self.fileEntry.setText(self.openfile)
	
	def import_button(self): 
		if not self.passwordEntry.text() == "":
			self.importing = Encryption()
			self.importing.import_from_file(self.openfile, self.username, self.passwordEntry.text(), self.password)
			self.importProgress.setProperty("value", 30)
			time.sleep(0.2)
			self.importProgress.setProperty("value", 100)
			QtWidgets.QMessageBox.information(self, "Import Successful", "Passwords Import Successful, Please Restart the Application to See the Changes\nOr Add a Blank Password, It'll Give you an Error, Press Ok, It'll Refresh")
			QtWidgets.QDialog.close(self)
		else:
			QtWidgets.QMessageBox.warning(self, "Password Empty", "Old user Password is needed For Decrypting.\nI can't Proceed Otherwise, If Password Wrong,\nI don't Know what Might happen")


#################################################################
################# EXPORTER DIALOG UI ############################
#################################################################
class Ui_ExportDialog(object):
	def setupUi(self, ExportDialog):
		self.ExportDialog = ExportDialog
		ExportDialog.setObjectName("ExportDialog")
		ExportDialog.resize(617, 250)
		ExportDialog.setMinimumSize(QtCore.QSize(617, 250))
		ExportDialog.setMaximumSize(QtCore.QSize(617, 250))
		ExportDialog.setStyleSheet("font: 10pt \"Cantarell\";")
		self.verticalLayoutWidget = QtWidgets.QWidget(ExportDialog)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 561, 191))
		self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
		self.mainLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
		self.mainLayout.setContentsMargins(0, 0, 0, 0)
		self.mainLayout.setObjectName("mainLayout")
		self.fileLayout = QtWidgets.QHBoxLayout()
		self.fileLayout.setObjectName("fileLayout")
		self.saveLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.saveLabel.setObjectName("saveLabel")
		self.fileLayout.addWidget(self.saveLabel)
		self.fileEntry = QtWidgets.QLineEdit(self.verticalLayoutWidget)
		self.fileEntry.setReadOnly(True)
		self.fileEntry.setObjectName("fileEntry")
		self.fileLayout.addWidget(self.fileEntry)
		self.browseButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.browseButton.setObjectName("browseButton")
		self.fileLayout.addWidget(self.browseButton)
		self.mainLayout.addLayout(self.fileLayout)
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem)
		self.exportButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.exportButton.setObjectName("exportButton")
		self.horizontalLayout.addWidget(self.exportButton)
		spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem1)
		self.mainLayout.addLayout(self.horizontalLayout)
		self.exportProgress = QtWidgets.QProgressBar(self.verticalLayoutWidget)
		self.exportProgress.setProperty("value", 0)
		self.exportProgress.setInvertedAppearance(False)
		self.exportProgress.setObjectName("exportProgress")
		self.mainLayout.addWidget(self.exportProgress)

		self.retranslateUi(ExportDialog)
		QtCore.QMetaObject.connectSlotsByName(ExportDialog)

	def retranslateUi(self, ExportDialog):
		_translate = QtCore.QCoreApplication.translate
		self._translate = _translate
		ExportDialog.setWindowTitle(_translate("ExportDialog", "Export Passwords"))
		self.saveLabel.setText(_translate("ExportDialog", "Save File:"))
		self.browseButton.setText(_translate("ExportDialog", "Browse"))
		self.exportButton.setText(_translate("ExportDialog", "Export"))

class ExportDialog_Ui(QtWidgets.QDialog, Ui_ExportDialog):
	def __init__(self, username, password, parent = None):
		QtWidgets.QDialog.__init__(self, parent)
		self.setupUi(self)
		self.username = username
		self.password = password
		self.finalize_ui()
		self.options = QtWidgets.QFileDialog.Options()
		self.options = QtWidgets.QFileDialog.DontUseNativeDialog
	
	def finalize_ui(self):
		self.browseButton.clicked.connect(self.browse_save_db_file)
		self.exportButton.clicked.connect(self.export_button)
	
	def browse_save_db_file(self):
		self.saveloc = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose Save Directory", ".", options = self.options)
		self.fileEntry.setText(self.saveloc)

	
	def export_button(self):
		self.exporting = Encryption()
		self.exporting.export_to_file(self.saveloc, self.username, self.password)
		self.exportProgress.setProperty("value", 30)
		time.sleep(0.2)
		self.exportProgress.setProperty("value", 100)
		QtWidgets.QDialog.close(self)
	

#################################################################
################# IMPORT EXPORT CLASS ###########################
#################################################################
class Encryption():
	
	def import_from_file(self, filename, username, password, newPassword):
		sqdata = self.read_from_sql(filename, password)
		newData = []
		userFile = os.path.join(".", "PyPasswordManager_files", f"{username}_passwords")
		dbFolder = os.path.join(".", "PyPasswordManager_files", "database", f"{username}_passwords.sqlite3")

		with shelve.open(userFile) as shfile:
			try:
				for item in list(shfile.keys()):
					del shfile[item]
			except:
				print("Nothing")
			for items in sqdata:
				dataDict = {"name": f"{items[0]}",
							"url": f"{items[1]}",
							"email": f"{items[2]}",
							"password": f"{items[3]}",
							"notes": f"{items[4]}"}

				shfile[dataDict["name"]] = {"name": f"{items[0]}",
											"url": f"{items[1]}",
											"email": self.encrypt_string(items[2], newPassword),
											"password": self.encrypt_string(items[3], newPassword),
											"notes": f"{items[4]}"}
				newData.append(dataDict)
		self.write_to_sql(newData, dbFolder, newPassword)


	def export_to_file(self, folder, username, password):
		filename = os.path.join(folder, f"{dt.now()}_{username}.sqlite3")
		userfile = os.path.join(".", "PyPasswordManager_files", f"{username}_passwords")
		dataList = []
		with shelve.open(userfile) as shfile:
			for key in list(shfile.keys()):
				dataList.append(shfile[key])
		newDataList = []
		for item in dataList:
			newName = item["name"]
			newUrl = item["url"]
			newEmail = self.decrypt_string(item["email"], password)
			newPassword = self.decrypt_string(item["password"], password)
			newNotes = item["notes"]
			
			newDataList.append([newName, newUrl, newEmail, newPassword, newNotes])
		
		self.write_to_sql(newDataList, filename, password)

	
	def encrypt_string(self, string, password):
		pw = bytes(password, 'utf-8')
		salt = b'\xdc\xe0~;f\x804\xe7\xa7\x8f\xa3\xafmPM\x01'
		kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=salt,iterations=100000)
		key = base64.urlsafe_b64encode(kdf.derive(pw))
		
		ferKey = Fernet(key)
		string = bytes(string, 'utf-8')
		token = str(ferKey.encrypt(string))
		token = token.removesuffix("'")
		token = token.removeprefix("b'")
		return token

	
	def decrypt_string(self, string, password):
		pw = bytes(password, 'utf-8')
		salt = b'\xdc\xe0~;f\x804\xe7\xa7\x8f\xa3\xafmPM\x01'
		kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=salt,iterations=100000)
		key = base64.urlsafe_b64encode(kdf.derive(pw))
		
		ferKey = Fernet(key)
		string = bytes(string, 'utf-8')
		token = str(ferKey.decrypt(string))
		token = token.removesuffix("'")
		token = token.removeprefix("b'")
		return token

	
	def write_to_sql(self, dataList, filename, password):
		sqconn = sq.connect(filename)
		sqcurs = sqconn.cursor()
		
		try:
			sqcurs.execute("DROP TABLE saveddata")
			sqconn.commit()
		except:
			print("HAHA, NEVER THERE")

		sqcurs.execute("CREATE TABLE saveddata (name VARCHAR(30), url VARCHAR(90), email VARCHAR(120), password VARCHAR(120), notes VARCHAR(120))")
		sqconn.commit()
		
		if type(dataList[0]) == dict:
			for item in dataList:
				user_name = item["name"]
				user_url = item["url"]
				user_email = self.encrypt_string(item["email"], password)
				user_password = self.encrypt_string(item["password"], password)
				user_notes = item["notes"]
				sqcurs.execute("INSERT INTO saveddata VALUES(?,?,?,?,?)", (user_name, user_url, user_email, user_password, user_notes))
				sqconn.commit()
		else:
			for item in dataList:
				user_name = item[0]
				user_url = item[1]
				user_email = self.encrypt_string(item[2], password)
				user_password = self.encrypt_string(item[3], password)
				user_notes = item[4]
				
				sqcurs.execute("INSERT INTO saveddata VALUES(?,?,?,?,?)", (user_name, user_url, user_email, user_password, user_notes))
				sqconn.commit()
		sqconn.commit()
		sqconn.close()
	
	def read_from_sql(self, filename, password):
		sqconn = sq.connect(filename)
		sqcurs = sqconn.cursor()
				
		sqcurs.execute("SELECT * FROM saveddata")
		sqdata = sqcurs.fetchall()
		sqconn.commit()
		sqconn.close()
		newData = []
		for item in sqdata:
			newname = item[0]
			newurl = item[1]
			newemail = str(self.decrypt_string(item[2], password)).removeprefix("b'")
			newemail = newemail.removesuffix("'")
			newpassword = str(self.decrypt_string(item[3], password)).removeprefix("b'")
			newpassword = newpassword.removesuffix("'")
			newnotes = item[4]
			
			newData.append([newname, newurl, newemail, newpassword, newnotes])
		return newData

	

#################################################################
################# STYLE SHEET ###################################
#################################################################
stylesheet = """QPushButton {
	background-color: #7289da;
	color: #eeeeee
}
QLineEdit {
	background-color: #2c2f33;
	color: #eeeeee
}
QLabel {
	background-color: #23272a;
	color: #eeeeee
}
QMenuBar {
	background-color: #23272a;
	color: #eeeeee
}
QListWidget {
	background-color: #2c2f33;
	color: #eeeeee
}
QCheckBox {
	background-color: #23272a;
	color: #eeeeee
}
QSpinBox {
	background-color: #2c2f33;
	color: #eeeeee
}
"""

#################################################################
################# MAIN EXECUTION ################################
#################################################################

if __name__ == "__main__":
	loginApp = QtWidgets.QApplication(sys.argv)
	loginui = LoginWindow()
	loginui.show()
	if os.name in ["Nt", "NT", "nt"]:
		loginui.setStyleSheet(stylesheet)
	loginApp.exec_()
	username = loginui.username
	password = loginui.password
	
	if username in [None, ""]:
		sys.exit()
	app = QtWidgets.QApplication(sys.argv)
	mainui = PasswordManager(username, password)
	mainui.show()
	if os.name in ["Nt", "NT", "nt"]:
		mainui.setStyleSheet(stylesheet)
	sys.exit(app.exec_())
