# _*_coding:utf-8_*_
# Author： Zachary
import pymysql
import serial
import time
import sys
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QMovie, QPixmap


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        global timer
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1073, 719)
        MainWindow.setStyleSheet("#MainWindow{border-image:url(./bc.png)}")
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(150, 30, 751, 71))
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 L")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.Temp_Field = QtWidgets.QLabel(self.centralwidget)
        self.Temp_Field.setGeometry(QtCore.QRect(60, 140, 571, 491))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.Temp_Field.setFont(font)
        self.Temp_Field.setAlignment(QtCore.Qt.AlignCenter)
        self.Temp_Field.setObjectName("Temp_Field")
        self.Temp_Equip1 = QtWidgets.QLineEdit(self.centralwidget)
        self.Temp_Equip1.setGeometry(QtCore.QRect(780, 170, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Temp_Equip1.setFont(font)
        self.Temp_Equip1.setText("")
        self.Temp_Equip1.setObjectName("Temp_Equip1")
        self.Label_Equip1 = QtWidgets.QLabel(self.centralwidget)
        self.Label_Equip1.setGeometry(QtCore.QRect(697, 170, 76, 31))
        self.Label_Equip1.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Equip1.setObjectName("Label_Equip1")
        self.Temp_Set1 = QtWidgets.QLineEdit(self.centralwidget)
        self.Temp_Set1.setGeometry(QtCore.QRect(690, 450, 81, 31))
        self.Temp_Set1.setAlignment(QtCore.Qt.AlignCenter)
        self.Temp_Set1.setObjectName("Temp_Set1")
        self.Temp_Set2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Temp_Set2.setGeometry(QtCore.QRect(780, 450, 81, 31))
        self.Temp_Set2.setAlignment(QtCore.Qt.AlignCenter)
        self.Temp_Set2.setObjectName("Temp_Set2")
        self.Temp_Set3 = QtWidgets.QLineEdit(self.centralwidget)
        self.Temp_Set3.setGeometry(QtCore.QRect(870, 450, 81, 31))
        self.Temp_Set3.setAlignment(QtCore.Qt.AlignCenter)
        self.Temp_Set3.setObjectName("Temp_Set3")
        self.Temp_Set4 = QtWidgets.QLineEdit(self.centralwidget)
        self.Temp_Set4.setGeometry(QtCore.QRect(960, 450, 81, 31))
        self.Temp_Set4.setAlignment(QtCore.Qt.AlignCenter)
        self.Temp_Set4.setObjectName("Temp_Set4")
        self.Temp_Equip2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Temp_Equip2.setGeometry(QtCore.QRect(780, 210, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Temp_Equip2.setFont(font)
        self.Temp_Equip2.setText("")
        self.Temp_Equip2.setObjectName("Temp_Equip2")
        self.Label_Equip2 = QtWidgets.QLabel(self.centralwidget)
        self.Label_Equip2.setGeometry(QtCore.QRect(697, 210, 76, 31))
        self.Label_Equip2.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Equip2.setObjectName("Label_Equip2")
        self.Temp_Equip3 = QtWidgets.QLineEdit(self.centralwidget)
        self.Temp_Equip3.setGeometry(QtCore.QRect(780, 250, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Temp_Equip3.setFont(font)
        self.Temp_Equip3.setText("")
        self.Temp_Equip3.setObjectName("Temp_Equip3")
        self.Label_Equip3 = QtWidgets.QLabel(self.centralwidget)
        self.Label_Equip3.setGeometry(QtCore.QRect(697, 250, 76, 31))
        self.Label_Equip3.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Equip3.setObjectName("Label_Equip3")
        self.Temp_Equip4 = QtWidgets.QLineEdit(self.centralwidget)
        self.Temp_Equip4.setGeometry(QtCore.QRect(780, 290, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Temp_Equip4.setFont(font)
        self.Temp_Equip4.setText("")
        self.Temp_Equip4.setObjectName("Temp_Equip4")
        self.Label_Equip4 = QtWidgets.QLabel(self.centralwidget)
        self.Label_Equip4.setGeometry(QtCore.QRect(697, 290, 76, 31))
        self.Label_Equip4.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Equip4.setObjectName("Label_Equip4")
        self.Label_SetTemp = QtWidgets.QLabel(self.centralwidget)
        self.Label_SetTemp.setGeometry(QtCore.QRect(690, 370, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Label_SetTemp.setFont(font)
        self.Label_SetTemp.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_SetTemp.setObjectName("Label_SetTemp")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(710, 430, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(800, 430, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(890, 430, 51, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(980, 430, 51, 16))
        self.label_4.setObjectName("label_4")
        self.Temp_Confirm = QtWidgets.QPushButton(self.centralwidget)
        self.Temp_Confirm.setGeometry(QtCore.QRect(920, 380, 93, 28))
        self.Temp_Confirm.setObjectName("Temp_Confirm")
        self.Temp_Warning = QtWidgets.QTextBrowser(self.centralwidget)
        self.Temp_Warning.setGeometry(QtCore.QRect(690, 490, 241, 151))
        self.Temp_Warning.setObjectName("Temp_Warning")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(950, 520, 101, 101))
        self.label_5.setStyleSheet("image: url(:/warning.gif);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1073, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Temp_threshold1 = self.Temp_Set1.text()
        self.Temp_threshold2 = self.Temp_Set2.text()
        self.Temp_threshold3 = self.Temp_Set3.text()
        self.Temp_threshold4 = self.Temp_Set4.text()

    def retranslateUi(self, MainWindow):
        global timer
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "温度监测系统 V1.0"))
        self.Title.setText(_translate("MainWindow", "欢迎使用牧场环境与个体温度监测系统"))
        self.Temp_Field.setText(_translate("MainWindow", "温度场显示"))
        self.Label_Equip1.setText(_translate("MainWindow", "设备1温度 "))
        self.Temp_Set1.setText(_translate("MainWindow", "37.0"))
        self.Temp_Set2.setText(_translate("MainWindow", "37.0"))
        self.Temp_Set3.setText(_translate("MainWindow", "37.0"))
        self.Temp_Set4.setText(_translate("MainWindow", "37.0"))
        self.Label_Equip2.setText(_translate("MainWindow", "设备2温度 "))
        self.Label_Equip3.setText(_translate("MainWindow", "设备3温度 "))
        self.Label_Equip4.setText(_translate("MainWindow", "设备4温度 "))
        self.Label_SetTemp.setText(_translate("MainWindow", "温度阈值设定"))
        self.label.setText(_translate("MainWindow", "阈值1"))
        self.label_2.setText(_translate("MainWindow", "阈值2"))
        self.label_3.setText(_translate("MainWindow", "阈值3"))
        self.label_4.setText(_translate("MainWindow", "阈值4"))
        self.Temp_Confirm.setText(_translate("MainWindow", "阈值设定"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))

        # 设定一个定时器，每隔5秒刷新显示的数据
        self.timer = QTimer()
        self.timer.start(5000)
        self.timer.timeout.connect(self.read_Db)

        # 设定另一个定时器，每隔5秒检查温度是否超出阈值
        self.timer2 = QTimer()
        self.timer2.start(10000)
        self.timer2.timeout.connect(self.temp_Warning)

        # 点击阈值设定按钮，将阈值设定好之后循环执行温度监测报警功能
        self.Temp_Confirm.clicked.connect(self.set_Temp)

        pixmap = QPixmap("fig.png")
        self.Temp_Field.setPixmap(pixmap)
        self.Temp_Field.setScaledContents(True)

    def read_Db(self):
        """
        连接数据库 并显示到指定区域
        :return:
        """
        conn = pymysql.connect(user='root', password='980226', database='power', use_unicode=True)
        cursor = conn.cursor()

        my_query = "select * from current order by id desc limit 1"
        ## de="delete from current where id=1"
        cursor.execute(my_query)
        results = cursor.fetchall()
        for row in results:
            temp1 = str(row[1])
            temp2 = str(row[2])
            temp3 = str(row[3])
            temp4 = str(row[4])
            self.Temp_Equip1.setText(temp1)
            self.Temp_Equip2.setText(temp2)
            self.Temp_Equip3.setText(temp3)
            self.Temp_Equip4.setText(temp4)

    def set_Temp(self):
        """
        设置温度阈值
        :return:
        """
        self.Temp_threshold1 = self.Temp_Set1.text()
        self.Temp_threshold2 = self.Temp_Set2.text()
        self.Temp_threshold3 = self.Temp_Set3.text()
        self.Temp_threshold4 = self.Temp_Set4.text()
        self.Temp_Warning.setText("温度阈值设定成功")
        # print("温度阈值设定成功")
        # print(f"温度阈值设定成功,设备1：{self.Temp_threshold1}  设备2：{self.Temp_threshold2}  设备3：{self.Temp_threshold3}  设备4：{self.Temp_threshold4}")

    def temp_Warning(self):
        """
        超过所设置的阈值即启动报警信号，每隔5秒检查一次
        :return:
        """
        self.Temp_Warning.setText("")
        flag = [0 for _ in range(4)]  #这个3是设备的个数 0代表无异常
        if self.Temp_Equip1.text() > self.Temp_threshold1:
            flag[0] = 1
            # self.Temp_Warning.setText("请注意，设备一温度异常！")
        if self.Temp_Equip2.text() > self.Temp_threshold2:
            flag[1] = 1
            # self.Temp_Warning.append("请注意，设备二温度异常！")
        if self.Temp_Equip3.text() > self.Temp_threshold3:
            flag[2] = 1
            # self.Temp_Warning.append("请注意，设备三温度异常！")
        if self.Temp_Equip4.text() > self.Temp_threshold4:
            flag[3] = 1
            # self.Temp_Warning.append("请注意，设备四温度异常！")

        for i in range(4):
            if flag[i] == 1:
                self.Temp_Warning.append(f"请注意，设备{i+1}的温度异常！")

        if flag == [0,0,0,0]:
            self.Temp_Warning.setText("温度正常")



def Listen_Tempdata():
    """
    这是监听温度的函数，串口号COM11 每隔5秒 将从串口监听到的数据写入数据库中
    :return:
    """
    conn = pymysql.connect(user='root', password='980226', database='power', use_unicode=True)
    cursor = conn.cursor()

    ser = serial.Serial(port='COM11', baudrate=9600, bytesize=8, parity=serial.PARITY_NONE, stopbits=1, timeout=2)
    # ask=b"\x01\x03\x00\x01\x00\x02\x95\xCB"
    ask = b"\x01\x03\x00\x00\x00\x10\x44\x06"
    while True:
        ser.write(ask)
        x = ser.readline()
        data = ":".join("{:02x}".format(c) for c in x)
        # print('data=', data)

        hex_data = data.split(':')
        # print('hex_data =', hex_data)
        #
        t1 = hex_data[5] + hex_data[6]
        t2 = hex_data[7] + hex_data[8]
        t3 = hex_data[9] + hex_data[10]
        t4 = hex_data[11] + hex_data[12]

        temp1 = str(int(t1, 16) / 10)
        temp2 = str(int(t2, 16) / 10)
        temp3 = str(int(t3, 16) / 10)
        temp4 = str(int(t4, 16) / 10)

        my_insert = "insert into `current`(`temp1`,`temp2`,`temp3`,`temp4`) values('%s','%s','%s','%s')" % (
            temp1, temp2, temp3, temp4)
        ## de="delete from current where id=1"
        cursor.execute(my_insert)
        print("写入成功")

        # print("一号监测点温度是", temp1, end="    ")
        # print("二号监测点温度是", temp2, end="    ")
        # print("三号监测点温度是", temp3)
        # print("=========================================")

        time.sleep(5)
        data = ""


def main_UI():
    """
    这里设置了一个多线程，用以启动UI界面
    :return:
    """
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()  # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_MainWindow()  # ui是Ui_MainWindow()类的实例化对象
    ui.setupUi(MainWindow)  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    MainWindow.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication


if __name__ == "__main__":
    Task1 = threading.Thread(target=main_UI)
    Task2 = threading.Thread(target=Listen_Tempdata)
    Task1.start()
    Task2.start()
