# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ggezj\PycharmProjects\Study\Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(874, 844)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 10, 820, 764))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_3.setSpacing(10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.original_photo = QtWidgets.QLabel(self.layoutWidget)
        self.original_photo.setEnabled(True)
        self.original_photo.setMinimumSize(QtCore.QSize(250, 250))
        self.original_photo.setMaximumSize(QtCore.QSize(250, 250))
        self.original_photo.setText("")
        self.original_photo.setObjectName("original_photo")
        self.verticalLayout_8.addWidget(self.original_photo, 0, QtCore.Qt.AlignTop)
        self.quality_label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.quality_label_2.setFont(font)
        self.quality_label_2.setObjectName("quality_label_2")
        self.verticalLayout_8.addWidget(self.quality_label_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.quality_slider_2 = QtWidgets.QSlider(self.layoutWidget)
        self.quality_slider_2.setEnabled(False)
        self.quality_slider_2.setMinimum(1)
        self.quality_slider_2.setMaximum(100)
        self.quality_slider_2.setSliderPosition(100)
        self.quality_slider_2.setOrientation(QtCore.Qt.Horizontal)
        self.quality_slider_2.setObjectName("quality_slider_2")
        self.verticalLayout_8.addWidget(self.quality_slider_2)
        self.resize_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.resize_label.setFont(font)
        self.resize_label.setObjectName("resize_label")
        self.verticalLayout_8.addWidget(self.resize_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.resize_slider = QtWidgets.QSlider(self.layoutWidget)
        self.resize_slider.setEnabled(False)
        self.resize_slider.setMinimum(1)
        self.resize_slider.setMaximum(100)
        self.resize_slider.setSliderPosition(100)
        self.resize_slider.setOrientation(QtCore.Qt.Horizontal)
        self.resize_slider.setObjectName("resize_slider")
        self.verticalLayout_8.addWidget(self.resize_slider)
        self.jpg_checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.jpg_checkBox_2.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.jpg_checkBox_2.setFont(font)
        self.jpg_checkBox_2.setObjectName("jpg_checkBox_2")
        self.verticalLayout_8.addWidget(self.jpg_checkBox_2)
        self.height_label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.height_label_2.setFont(font)
        self.height_label_2.setObjectName("height_label_2")
        self.verticalLayout_8.addWidget(self.height_label_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.height_edit_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.height_edit_line.setEnabled(False)
        self.height_edit_line.setObjectName("height_edit_line")
        self.verticalLayout_8.addWidget(self.height_edit_line)
        self.width_label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.width_label_2.setFont(font)
        self.width_label_2.setObjectName("width_label_2")
        self.verticalLayout_8.addWidget(self.width_label_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.width_edit_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.width_edit_line.setEnabled(False)
        self.width_edit_line.setObjectName("width_edit_line")
        self.verticalLayout_8.addWidget(self.width_edit_line)
        self.compressButton = QtWidgets.QPushButton(self.layoutWidget)
        self.compressButton.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.compressButton.setFont(font)
        self.compressButton.setObjectName("compressButton")
        self.verticalLayout_8.addWidget(self.compressButton)
        self.scrollArea = QtWidgets.QScrollArea(self.layoutWidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(250, 55))
        self.scrollArea.setMaximumSize(QtCore.QSize(250, 55))
        self.scrollArea.setSizeIncrement(QtCore.QSize(0, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 231, 80))
        self.scrollAreaWidgetContents_2.setMinimumSize(QtCore.QSize(150, 80))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.original_photo_info_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.original_photo_info_2.setGeometry(QtCore.QRect(0, 10, 230, 40))
        self.original_photo_info_2.setMinimumSize(QtCore.QSize(230, 40))
        self.original_photo_info_2.setMaximumSize(QtCore.QSize(230, 35))
        self.original_photo_info_2.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.original_photo_info_2.setFont(font)
        self.original_photo_info_2.setText("")
        self.original_photo_info_2.setWordWrap(True)
        self.original_photo_info_2.setObjectName("original_photo_info_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_8.addWidget(self.scrollArea)
        self.gridLayout_3.addLayout(self.verticalLayout_8, 0, 0, 1, 1)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_9.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.compressed_photo = QtWidgets.QLabel(self.layoutWidget)
        self.compressed_photo.setMinimumSize(QtCore.QSize(500, 150))
        self.compressed_photo.setMaximumSize(QtCore.QSize(500, 150))
        self.compressed_photo.setText("")
        self.compressed_photo.setObjectName("compressed_photo")
        self.verticalLayout_9.addWidget(self.compressed_photo)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.red_height_lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.red_height_lineEdit_2.setFont(font)
        self.red_height_lineEdit_2.setObjectName("red_height_lineEdit_2")
        self.gridLayout_8.addWidget(self.red_height_lineEdit_2, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_8.addWidget(self.label_9, 1, 0, 1, 1)
        self.red_width_lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.red_width_lineEdit_2.setFont(font)
        self.red_width_lineEdit_2.setObjectName("red_width_lineEdit_2")
        self.gridLayout_8.addWidget(self.red_width_lineEdit_2, 2, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_8.addWidget(self.label_10, 2, 0, 1, 1)
        self.red_luminosity_button = QtWidgets.QPushButton(self.layoutWidget)
        self.red_luminosity_button.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.red_luminosity_button.setFont(font)
        self.red_luminosity_button.setObjectName("red_luminosity_button")
        self.gridLayout_8.addWidget(self.red_luminosity_button, 3, 0, 1, 2)
        self.gridLayout_6.addLayout(self.gridLayout_8, 0, 1, 1, 1)
        self.photo_red_2 = QtWidgets.QLabel(self.layoutWidget)
        self.photo_red_2.setMinimumSize(QtCore.QSize(300, 150))
        self.photo_red_2.setMaximumSize(QtCore.QSize(300, 150))
        self.photo_red_2.setText("")
        self.photo_red_2.setObjectName("photo_red_2")
        self.gridLayout_6.addWidget(self.photo_red_2, 0, 0, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout_6)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.photo_green_2 = QtWidgets.QLabel(self.layoutWidget)
        self.photo_green_2.setMinimumSize(QtCore.QSize(300, 150))
        self.photo_green_2.setMaximumSize(QtCore.QSize(300, 150))
        self.photo_green_2.setText("")
        self.photo_green_2.setObjectName("photo_green_2")
        self.gridLayout_7.addWidget(self.photo_green_2, 0, 0, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.green_width_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.green_width_lineEdit.setFont(font)
        self.green_width_lineEdit.setObjectName("green_width_lineEdit")
        self.gridLayout_9.addWidget(self.green_width_lineEdit, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_9.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_9.addWidget(self.label_5, 0, 0, 1, 1)
        self.green_height_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.green_height_lineEdit.setFont(font)
        self.green_height_lineEdit.setObjectName("green_height_lineEdit")
        self.gridLayout_9.addWidget(self.green_height_lineEdit, 0, 1, 1, 1)
        self.green_luminosity_button = QtWidgets.QPushButton(self.layoutWidget)
        self.green_luminosity_button.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.green_luminosity_button.setFont(font)
        self.green_luminosity_button.setObjectName("green_luminosity_button")
        self.gridLayout_9.addWidget(self.green_luminosity_button, 2, 0, 1, 2)
        self.gridLayout_7.addLayout(self.gridLayout_9, 0, 1, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout_7)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.photo_blue_2 = QtWidgets.QLabel(self.layoutWidget)
        self.photo_blue_2.setMinimumSize(QtCore.QSize(300, 150))
        self.photo_blue_2.setMaximumSize(QtCore.QSize(300, 150))
        self.photo_blue_2.setText("")
        self.photo_blue_2.setObjectName("photo_blue_2")
        self.gridLayout_4.addWidget(self.photo_blue_2, 0, 0, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.blue_height_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.blue_height_lineEdit.setFont(font)
        self.blue_height_lineEdit.setObjectName("blue_height_lineEdit")
        self.gridLayout_10.addWidget(self.blue_height_lineEdit, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_10.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_10.addWidget(self.label_8, 1, 0, 1, 1)
        self.blue_width_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.blue_width_lineEdit.setFont(font)
        self.blue_width_lineEdit.setObjectName("blue_width_lineEdit")
        self.gridLayout_10.addWidget(self.blue_width_lineEdit, 1, 1, 1, 1)
        self.blue_luminosity_button = QtWidgets.QPushButton(self.layoutWidget)
        self.blue_luminosity_button.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.blue_luminosity_button.setFont(font)
        self.blue_luminosity_button.setObjectName("blue_luminosity_button")
        self.gridLayout_10.addWidget(self.blue_luminosity_button, 2, 0, 1, 2)
        self.gridLayout_4.addLayout(self.gridLayout_10, 0, 1, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout_4)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.layoutWidget)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(500, 80))
        self.scrollArea_2.setMaximumSize(QtCore.QSize(500, 80))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 481, 100))
        self.scrollAreaWidgetContents_3.setMinimumSize(QtCore.QSize(150, 100))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.compressed_photo_info_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.compressed_photo_info_2.setGeometry(QtCore.QRect(0, 10, 480, 60))
        self.compressed_photo_info_2.setMinimumSize(QtCore.QSize(480, 60))
        self.compressed_photo_info_2.setMaximumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.compressed_photo_info_2.setFont(font)
        self.compressed_photo_info_2.setText("")
        self.compressed_photo_info_2.setWordWrap(True)
        self.compressed_photo_info_2.setObjectName("compressed_photo_info_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_9.addWidget(self.scrollArea_2)
        self.gridLayout_3.addLayout(self.verticalLayout_9, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 874, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_File)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " Image Compression"))
        self.label_2.setText(_translate("MainWindow", "Original photo"))
        self.quality_label_2.setText(_translate("MainWindow", "Quality: 100"))
        self.resize_label.setText(_translate("MainWindow", "Resizing ratio: 100"))
        self.jpg_checkBox_2.setText(_translate("MainWindow", "Convert to jpg"))
        self.height_label_2.setText(_translate("MainWindow", "Height"))
        self.width_label_2.setText(_translate("MainWindow", "Width"))
        self.compressButton.setText(_translate("MainWindow", "Compress"))
        self.label.setText(_translate("MainWindow", "Compressed photo"))
        self.label_9.setText(_translate("MainWindow", "y1,y2"))
        self.label_10.setText(_translate("MainWindow", "x1,x2"))
        self.red_luminosity_button.setText(_translate("MainWindow", "Open Red Chanel Graphic"))
        self.label_6.setText(_translate("MainWindow", "x1,x2"))
        self.label_5.setText(_translate("MainWindow", "y1,y2"))
        self.green_luminosity_button.setText(_translate("MainWindow", "Open Green Chanel Graphic"))
        self.label_7.setText(_translate("MainWindow", "y1,y2"))
        self.label_8.setText(_translate("MainWindow", "x1,x2"))
        self.blue_luminosity_button.setText(_translate("MainWindow", "Open Blue Chanel Graphic"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())