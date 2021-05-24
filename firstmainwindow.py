# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstmainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import os
import sys
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_firstMainWindow(object):
    def setupUi(self, firstMainWindow):
        firstMainWindow.setObjectName("firstMainWindow")
        firstMainWindow.resize(682, 433)
        firstMainWindow.setStyleSheet("#firstMainWindow{border-image:url(./first_bc.png)}")
        self.centralwidget = QtWidgets.QWidget(firstMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 70, 681, 61))
        font = QtGui.QFont()
        font.setFamily("华文中宋")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.userinput = QtWidgets.QLineEdit(self.centralwidget)
        self.userinput.setGeometry(QtCore.QRect(320, 200, 141, 31))
        self.userinput.setObjectName("userinput")
        self.passwordinput = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordinput.setGeometry(QtCore.QRect(320, 250, 141, 31))
        self.passwordinput.setObjectName("passwordinput")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(211, 200, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 250, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(370, 330, 61, 28))
        self.login.setObjectName("login")
        self.assign = QtWidgets.QPushButton(self.centralwidget)
        self.assign.setGeometry(QtCore.QRect(240, 330, 61, 28))
        self.assign.setObjectName("assign")
        firstMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(firstMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 682, 26))
        self.menubar.setObjectName("menubar")
        firstMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(firstMainWindow)
        self.statusbar.setObjectName("statusbar")
        firstMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(firstMainWindow)
        QtCore.QMetaObject.connectSlotsByName(firstMainWindow)

    def retranslateUi(self, firstMainWindow):
        _translate = QtCore.QCoreApplication.translate
        firstMainWindow.setWindowTitle(_translate("firstMainWindow", "请登录"))
        self.label.setText(_translate("firstMainWindow", "请登录温度监测系统"))
        self.label_2.setText(_translate("firstMainWindow", "用户名"))
        self.label_3.setText(_translate("firstMainWindow", "密 码"))
        self.login.setText(_translate("firstMainWindow", "登录"))
        self.assign.setText(_translate("firstMainWindow", "注册"))

        self.login.clicked.connect(self.login_clicked)
        self.assign.clicked.connect(self.assign_clicked)

    def login_clicked(self):
        conn = pymysql.connect(user='root', password='980226', database='power', use_unicode=True)
        cursor = conn.cursor()

        name = self.userinput.text()
        password = self.passwordinput.text()

        if not name and not password:
            msg_box = QMessageBox(QMessageBox.Warning, "提示", "请输入用户名和密码!")
            msg_box.exec_()
            return

        name = self.userinput.text()
        password = self.passwordinput.text()
        my_query = f"select * from user where username = %s"
        ## de="delete from current where id=1"
        cursor.execute(my_query, [name])
        results = cursor.fetchall()

        if results:
            my_query = f"select * from user where username = %s and userpassword =%s"
            ## de="delete from current where id=1"
            cursor.execute(my_query, [name, password])
            results = cursor.fetchall()
            if results:
                os.system("python mainwindow.py")
                sys.exit(self.exec_())
            else:
                msg_box = QMessageBox(QMessageBox.Warning, "提示", "密码错误，请重试!")
                msg_box.exec_()

        else:
            msg_box = QMessageBox(QMessageBox.Warning, "提示", "用户名不存在请先注册!")
            msg_box.exec_()

    def assign_clicked(self):
        conn = pymysql.connect(user='root', password='980226', database='power', use_unicode=True)
        cursor = conn.cursor()

        name = self.userinput.text()
        password = self.passwordinput.text()

        my_query = "insert into user (username,userpassword) values (%s,%s)"
        cursor.execute(my_query,(name,password))
        conn.commit()

        msg_box = QMessageBox(QMessageBox.Warning, "提示", "用户注册成功!")
        msg_box.exec_()


def first_main_UI():
    """
    这里设置了一个多线程，用以启动UI界面
    :return:
    """
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()  # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_firstMainWindow()  # ui是Ui_MainWindow()类的实例化对象
    ui.setupUi(MainWindow)  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    MainWindow.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication


if __name__ == "__main__":
    first_main_UI()
