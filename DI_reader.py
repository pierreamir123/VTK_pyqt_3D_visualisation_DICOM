# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be los
from PyQt5 import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout , QShortcut, QLabel, QSlider, QStyle, QSizePolicy, QFileDialog
import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor as qvtk



        


class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.setWindowModality(QtCore.Qt.WindowModal)
                MainWindow.resize(804, 586)
                MainWindow.setAutoFillBackground(True)
                MainWindow.setStyleSheet("background:rgb(91,90,90)")
                MainWindow.setDocumentMode(True)
                MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
                MainWindow.setDockNestingEnabled(True)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setAutoFillBackground(True)
                self.centralwidget.setObjectName("centralwidget")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.tabw = QtWidgets.QTabWidget(self.centralwidget)
                self.tabw.setAutoFillBackground(False)
                self.tabw.setStyleSheet("background:rgb(91,90,90)")
                self.tabw.setObjectName("tabw")
                self.tab = QtWidgets.QWidget()
                self.tab.setObjectName("tab")
                self.label = QtWidgets.QLabel(self.tab)
                self.label.setGeometry(QtCore.QRect(240, 10, 261, 31))
                self.label.setObjectName("label")
                self.sr_iso_box = QtWidgets.QGroupBox(self.tab)
                self.sr_iso_box.setGeometry(QtCore.QRect(430, 180, 301, 101))
                self.sr_iso_box.setStyleSheet("QGroupBox{\n"
        "    border:1px solid rgb(51,51,51);    \n"
        "    border-radius:4px;\n"
        "    color:white;\n"
        "    background:rgb(91,90,90);\n"
        "}")
                self.sr_iso_box.setObjectName("sr_iso_box")
                self.sr_iso_tbox = QtWidgets.QPlainTextEdit(self.sr_iso_box)
                self.sr_iso_tbox.setGeometry(QtCore.QRect(10, 40, 71, 31))
                self.sr_iso_tbox.setStyleSheet("background-color: rgb(255, 250, 226);\n"
        "font: 75 8pt \"Orbitron\";")
                self.sr_iso_tbox.setObjectName("sr_iso_tbox")
                self.sr_iso_slider = QtWidgets.QSlider(self.sr_iso_box)
                self.sr_iso_slider.setGeometry(QtCore.QRect(90, 40, 201, 31))
                self.sr_iso_slider.setStyleSheet("QSlider::groove:horizontal {\n"
        "        height:5px;\n"
        "        background: rgb(51,51,51);\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "        background:rgb(0,143,170);\n"
        "        width: 10px;\n"
        "    margin:-8px 0\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizondal {\n"
        "        background:rgb(51,51,51);\n"
        "}\n"
        "\n"
        "QSlider::sub-page:horizondal {\n"
        "        background:rgb(51,51,51);\n"
        "}")
                self.sr_iso_slider.setOrientation(QtCore.Qt.Horizontal)
                self.sr_iso_slider.setObjectName("sr_iso_slider")
                self.sr_import_box = QtWidgets.QGroupBox(self.tab)
                self.sr_import_box.setGeometry(QtCore.QRect(430, 60, 301, 101))
                self.sr_import_box.setStyleSheet("QGroupBox{\n"
        "    border:1px solid rgb(51,51,51);    \n"
        "    border-radius:4px;\n"
        "    color:white;\n"
        "    background:rgb(91,90,90);\n"
        "}")
                self.sr_import_box.setObjectName("sr_import_box")
                self.sr_browse = QtWidgets.QPushButton(self.sr_import_box)
                self.sr_browse.setGeometry(QtCore.QRect(210, 40, 75, 31))
                self.sr_browse.setStyleSheet("QPushButton {\n"
        "    border: 2px solid rgb(51,51,51);\n"
        "    border-radius: 5px;    \n"
        "    color:rgb(255,255,255);\n"
        "    background-color: rgb(51,51,51);\n"
        "}\n"
        "QPushButton:hover {\n"
        "    border: 2px solid rgb(0,143,150);\n"
        "    background-color: rgb(0,143,150);\n"
        "}\n"
        "QPushButton:pressed {    \n"
        "    border: 2px solid rgb(0,143,150);\n"
        "    background-color: rgb(51,51,51);\n"
        "}\n"
        "\n"
        "QPushButton:disabled {    \n"
        "    border-radius: 5px;    \n"
        "    border: 2px solid rgb(112,112,112);\n"
        "    background-color: rgb(112,112,112);\n"
        "}")
                self.sr_browse.setObjectName("sr_browse")
                self.sr_import_tb = QtWidgets.QPlainTextEdit(self.sr_import_box)
                self.sr_import_tb.setGeometry(QtCore.QRect(10, 40, 191, 31))
                self.sr_import_tb.setStyleSheet("background-color: rgb(255, 250, 226);\n"
        "font: 75 8pt \"Orbitron\";")
                self.sr_import_tb.setObjectName("sr_import_tb")
                self.sr_rgb_box = QtWidgets.QGroupBox(self.tab)
                self.sr_rgb_box.setGeometry(QtCore.QRect(430, 310, 301, 171))
                self.sr_rgb_box.setStyleSheet("QGroupBox{\n"
        "    border:1px solid rgb(51,51,51);    \n"
        "    border-radius:4px;\n"
        "    color:white;\n"
        "    background:rgb(91,90,90);\n"
        "}")
                self.sr_rgb_box.setObjectName("sr_rgb_box")
                self.sr_red_slider = QtWidgets.QSlider(self.sr_rgb_box)
                self.sr_red_slider.setGeometry(QtCore.QRect(90, 30, 201, 31))
                self.sr_red_slider.setStyleSheet("QSlider::groove:horizontal {\n"
        "        height:5px;\n"
        "        background: rgb(51,51,51);\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "        background:rgb(0,143,170);\n"
        "        width: 10px;\n"
        "    margin:-8px 0\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizondal {\n"
        "        background:rgb(51,51,51);\n"
        "}\n"
        "\n"
        "QSlider::sub-page:horizondal {\n"
        "        background:rgb(51,51,51);\n"
        "}")
                self.sr_red_slider.setOrientation(QtCore.Qt.Horizontal)
                self.sr_red_slider.setObjectName("sr_red_slider")
                self.sr_green_slider = QtWidgets.QSlider(self.sr_rgb_box)
                self.sr_green_slider.setGeometry(QtCore.QRect(90, 70, 201, 31))
                self.sr_green_slider.setStyleSheet("QSlider::groove:horizontal {\n"
        "        height:5px;\n"
        "        background: rgb(51,51,51);\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "        background:rgb(0,143,170);\n"
        "        width: 10px;\n"
        "    margin:-8px 0\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizondal {\n"
        "        background:rgb(51,51,51);\n"
        "}\n"
        "\n"
        "QSlider::sub-page:horizondal {\n"
        "        background:rgb(51,51,51);\n"
        "}")
                self.sr_green_slider.setOrientation(QtCore.Qt.Horizontal)
                self.sr_green_slider.setObjectName("sr_green_slider")
                self.sr_blue_slider = QtWidgets.QSlider(self.sr_rgb_box)
                self.sr_blue_slider.setGeometry(QtCore.QRect(90, 110, 201, 31))
                self.sr_blue_slider.setStyleSheet("QSlider::groove:horizontal {\n"
        "        height:5px;\n"
        "        background: rgb(51,51,51);\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "        background:rgb(0,143,170);\n"
        "        width: 10px;\n"
        "    margin:-8px 0\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizondal {\n"
        "        background:rgb(51,51,51);\n"
        "}\n"
        "\n"
        "QSlider::sub-page:horizondal {\n"
        "        background:rgb(51,51,51);\n"
        "}")
                self.sr_blue_slider.setOrientation(QtCore.Qt.Horizontal)
                self.sr_blue_slider.setObjectName("sr_blue_slider")
                self.sr_red = QtWidgets.QLabel(self.sr_rgb_box)
                self.sr_red.setGeometry(QtCore.QRect(16, 30, 51, 31))
                self.sr_red.setObjectName("sr_red")
                self.sr_blue = QtWidgets.QLabel(self.sr_rgb_box)
                self.sr_blue.setGeometry(QtCore.QRect(16, 110, 51, 31))
                self.sr_blue.setObjectName("sr_blue")
                self.sr_green = QtWidgets.QLabel(self.sr_rgb_box)
                self.sr_green.setGeometry(QtCore.QRect(10, 70, 61, 31))
                self.sr_green.setObjectName("sr_green")
                self.sr_window_box = QtWidgets.QGroupBox(self.tab)
                self.sr_window_box.setGeometry(QtCore.QRect(10, 60, 411, 451))
                self.sr_window_box.setObjectName("sr_window_box")
                self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.sr_window_box)
                self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 391, 421))
                self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
                self.sr_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
                self.sr_layout.setContentsMargins(0, 0, 0, 0)
                self.sr_layout.setObjectName("sr_layout")
                self.tabw.addTab(self.tab, "")
                self.tab_2 = QtWidgets.QWidget()
                self.tab_2.setObjectName("tab_2")
                self.rc_iso_box = QtWidgets.QGroupBox(self.tab_2)
                self.rc_iso_box.setGeometry(QtCore.QRect(430, 179, 301, 101))
                self.rc_iso_box.setStyleSheet("QGroupBox{\n"
        "    border:1px solid rgb(51,51,51);    \n"
        "    border-radius:4px;\n"
        "    color:white;\n"
        "    background:rgb(91,90,90);\n"
                
        "}")
                self.rc_iso_box.setObjectName("rc_iso_box")
                self.rc_iso_slider = QtWidgets.QSlider(self.rc_iso_box)
                self.rc_iso_slider.setGeometry(QtCore.QRect(90, 40, 201, 31))
                self.rc_iso_slider.setStyleSheet("QSlider::groove:horizontal {\n"
        "        height:5px;\n"
        "        background: rgb(51,51,51);\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "        background:rgb(0,143,170);\n"
        "        width: 10px;\n"
        "    margin:-8px 0\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizondal {\n"
        "        background:rgb(51,51,51);\n"
        "}\n"
        "\n"
        "QSlider::sub-page:horizondal {\n"
        "        background:rgb(51,51,51);\n"
        "}")
                self.rc_iso_slider.setOrientation(QtCore.Qt.Horizontal)
                self.rc_iso_slider.setObjectName("rc_iso_slider")
                self.rc_iso_comboBox = QtWidgets.QComboBox(self.rc_iso_box)
                self.rc_iso_comboBox.setGeometry(QtCore.QRect(10, 40, 71, 31))
                self.rc_iso_comboBox.setStyleSheet("QComboBox {\n"
        "    border: 2px solid rgb(51,51,51);\n"
        "    border-radius: 5px;    \n"
        "    color:rgb(255,255,255);\n"
        "    background-color: rgb(51,51,51);\n"
        "}\n"
        "\n"
        "QComboBox:hover {\n"
        "    border: 2px solid rgb(0,143,170);\n"
        "    border-radius: 5px;    \n"
        "    color:rgb(255,255,255);\n"
        "    background-color: rgb(0,143,170);\n"
        "}\n"
        "\n"
        "QComboBox:!editable, QComboBox::drop-down:editable {\n"
        "    background: rgb(51,51,51);\n"
        "}\n"
        "\n"
        "QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
        "        background:rgb(51,51,51);\n"
        "}\n"
        "\n"
        "QComboBox:on { /* shift the text when the popup opens */\n"
        "        padding-top: 3px;\n"
        "        padding-left: 4px;\n"
        "}\n"
        "\n"
        "QComboBox::drop-down {\n"
        "        subcontrol-origin: padding;\n"
        "        subcontrol-position: top right;\n"
        "        width: 15px;\n"
        "\n"
        "        border-left-width: 1px;\n"
        "        border-left-color: darkgray;\n"
        "        border-left-style: solid; /* just a single line */\n"
        "        border-top-right-radius: 5px; /* same radius as the QComboBox */\n"
        "        border-bottom-right-radius: 5px;\n"
        "}\n"
        "\n"
        "\n"
        "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
        "        top: 1px;\n"
        "        left: 1px;\n"
        "}\n"
        "\n"
        "QComboBox::drop-down {\n"
        "        background:rgb(51,51,51);\n"
        "}")
                self.rc_iso_comboBox.setObjectName("rc_iso_comboBox")
                self.rc_iso_comboBox.addItem("skin1")
                self.rc_iso_comboBox.addItem("skin2")
                self.rc_iso_comboBox.addItem("tissue")
                self.rc_iso_comboBox.addItem("bones")
                self.rc_iso_comboBox.addItem("dense bones")
                self.label_5 = QtWidgets.QLabel(self.tab_2)
                self.label_5.setGeometry(QtCore.QRect(249, 9, 261, 31))
                self.label_5.setObjectName("label_5")
                self.rc_import_box = QtWidgets.QGroupBox(self.tab_2)
                self.rc_import_box.setGeometry(QtCore.QRect(430, 59, 301, 101))
                self.rc_import_box.setStyleSheet("QGroupBox{\n"
        "    border:1px solid rgb(51,51,51);    \n"
        "    border-radius:4px;\n"
        "    color:white;\n"
        "    background:rgb(91,90,90);\n"
        "}")
                self.rc_import_box.setObjectName("rc_import_box")
                self.rc_browse = QtWidgets.QPushButton(self.rc_import_box)
                self.rc_browse.setGeometry(QtCore.QRect(210, 40, 75, 31))
                self.rc_browse.setStyleSheet("QPushButton {\n"
        "    border: 2px solid rgb(51,51,51);\n"
        "    border-radius: 5px;    \n"
        "    color:rgb(255,255,255);\n"
        "    background-color: rgb(51,51,51);\n"
        "}\n"
        "QPushButton:hover {\n"
        "    border: 2px solid rgb(0,143,150);\n"
        "    background-color: rgb(0,143,150);\n"
        "}\n"
        "QPushButton:pressed {    \n"
        "    border: 2px solid rgb(0,143,150);\n"
        "    background-color: rgb(51,51,51);\n"
        "}\n"
        "\n"
        "QPushButton:disabled {    \n"
        "    border-radius: 5px;    \n"
        "    border: 2px solid rgb(112,112,112);\n"
        "    background-color: rgb(112,112,112);\n"
        "}")
                self.rc_browse.setObjectName("rc_browse")
                self.rc_import_tb = QtWidgets.QPlainTextEdit(self.rc_import_box)
                self.rc_import_tb.setGeometry(QtCore.QRect(10, 40, 191, 31))
                self.rc_import_tb.setStyleSheet("background-color: rgb(255, 250, 226);\n"
        "font: 75 8pt \"Orbitron\";")
                self.rc_import_tb.setObjectName("rc_import_tb")
                self.rc_rgb_box = QtWidgets.QGroupBox(self.tab_2)
                self.rc_rgb_box.setGeometry(QtCore.QRect(430, 309, 301, 171))
                self.rc_rgb_box.setStyleSheet("QGroupBox{\n"
        "    border:1px solid rgb(51,51,51);    \n"
        "    border-radius:4px;\n"
        "    color:white;\n"
        "    background:rgb(91,90,90);\n"
        "}")
                self.rc_rgb_box.setObjectName("rc_rgb_box")
                self.rc_red_slider = QtWidgets.QSlider(self.rc_rgb_box)
                self.rc_red_slider.setGeometry(QtCore.QRect(90, 30, 201, 31))
                self.rc_red_slider.setStyleSheet("QSlider::groove:horizontal {\n"
        "        height:5px;\n"
        "        background: rgb(51,51,51);\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "        background:rgb(0,143,170);\n"
        "        width: 10px;\n"
        "    margin:-8px 0\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizondal {\n"
        "        background:rgb(51,51,51);\n"
        "}\n"
        "\n"
        "QSlider::sub-page:horizondal {\n"
        "        background:rgb(51,51,51);\n"
        "}")
                self.rc_red_slider.setOrientation(QtCore.Qt.Horizontal)
                self.rc_red_slider.setObjectName("rc_red_slider")
                self.rc_green_slider = QtWidgets.QSlider(self.rc_rgb_box)
                self.rc_green_slider.setGeometry(QtCore.QRect(90, 70, 201, 31))
                self.rc_green_slider.setStyleSheet("QSlider::groove:horizontal {\n"
        "        height:5px;\n"
        "        background: rgb(51,51,51);\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "        background:rgb(0,143,170);\n"
        "        width: 10px;\n"
        "    margin:-8px 0\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizondal {\n"
        "        background:rgb(51,51,51);\n"
        "}\n"
        "\n"
        "QSlider::sub-page:horizondal {\n"
        "        background:rgb(51,51,51);\n"
        "}")
                self.rc_green_slider.setOrientation(QtCore.Qt.Horizontal)
                self.rc_green_slider.setObjectName("rc_green_slider")
                self.rc_blue_slider = QtWidgets.QSlider(self.rc_rgb_box)
                self.rc_blue_slider.setGeometry(QtCore.QRect(90, 110, 201, 31))
                self.rc_blue_slider.setStyleSheet("QSlider::groove:horizontal {\n"
        "        height:5px;\n"
        "        background: rgb(51,51,51);\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "        background:rgb(0,143,170);\n"
        "        width: 10px;\n"
        "    margin:-8px 0\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizondal {\n"
        "        background:rgb(51,51,51);\n"
        "}\n"
        "\n"
        "QSlider::sub-page:horizondal {\n"
        "        background:rgb(51,51,51);\n"
        "}")
                self.rc_blue_slider.setOrientation(QtCore.Qt.Horizontal)
                self.rc_blue_slider.setObjectName("rc_blue_slider")
                self.rc_red = QtWidgets.QLabel(self.rc_rgb_box)
                self.rc_red.setGeometry(QtCore.QRect(16, 30, 51, 31))
                self.rc_red.setObjectName("rc_red")
                self.rc_blue = QtWidgets.QLabel(self.rc_rgb_box)
                self.rc_blue.setGeometry(QtCore.QRect(16, 110, 51, 31))
                self.rc_blue.setObjectName("rc_blue")
                self.rc_green = QtWidgets.QLabel(self.rc_rgb_box)
                self.rc_green.setGeometry(QtCore.QRect(10, 70, 61, 31))
                self.rc_green.setObjectName("rc_green")
                self.rc_window_box = QtWidgets.QGroupBox(self.tab_2)
                self.rc_window_box.setGeometry(QtCore.QRect(10, 60, 411, 451))
                self.rc_window_box.setObjectName("rc_window_box")
                self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.rc_window_box)
                self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 391, 421))
                self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
                self.rc_window_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
                self.rc_window_layout.setContentsMargins(0, 0, 0, 0)
                self.rc_window_layout.setObjectName("rc_window_layout")
                self.tabw.addTab(self.tab_2, "")
                self.horizontalLayout_2.addWidget(self.tabw)
                self.verticalLayout_2.addLayout(self.horizontalLayout_2)
                MainWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.sr_browse.clicked.connect(lambda:self.get_file(0))
                self.rc_browse.clicked.connect(lambda:self.get_file(1))
                self.sro_vtk = ""
                sr_RGB_sliders = [self.sr_red_slider,self.sr_green_slider,self.sr_blue_slider]
                for s in sr_RGB_sliders:
                        self.setting_slider(s,1)
                rc_RGB_sliders = [self.rc_iso_slider ,self.rc_red_slider,self.rc_green_slider,self.rc_blue_slider]
                for s in rc_RGB_sliders:
                        self.setting_slider(s,1)
                self.setting_slider(self.sr_iso_slider,0)
                self.sr_iso_slider.valueChanged.connect(self.sr_value_changer)
                self.sr_red_slider.valueChanged.connect(self.sr_value_changer)
                self.sr_green_slider.valueChanged.connect(self.sr_value_changer)
                self.sr_blue_slider.valueChanged.connect(self.sr_value_changer)

                self.rc_iso_slider.valueChanged.connect(self.rc_value_changer)
                self.rc_red_slider.valueChanged.connect(self.rc_value_changer)
                self.rc_green_slider.valueChanged.connect(self.rc_value_changer)
                self.rc_blue_slider.valueChanged.connect(self.rc_value_changer)

                self.denisty_dic={'skin1': 1 , 'skin2':100 , 'tissue':500 , 'bones':1000 , 'dense bones':1500   }
                
                
                self.retranslateUi(MainWindow)
                self.tabw.setCurrentIndex(1)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)




        def get_file(self,typee):
                if(typee == 0):
                        for i in reversed(range(self.sr_layout.count())): 
                                self.sr_layout.itemAt(i).widget().deleteLater()
                        file = QFileDialog.getExistingDirectory()
                        self.sr_import_tb.setPlainText(file)
                        self.sro_vtk = vtk_W(file)
                        self.sro_vtk.surface_rendering()
                        self.sr_layout.addWidget(self.sro_vtk.frame)
                if(typee == 1):
                        for i in reversed(range(self.rc_window_layout.count())): 
                                self.rc_window_layout.itemAt(i).widget().deleteLater()
                        file = QFileDialog.getExistingDirectory()
                        self.rc_import_tb.setPlainText(file)
                        self.rc_vtk = vtk_W(file)
                        self.rc_vtk.ray_casting()
                        self.rc_window_layout.addWidget(self.rc_vtk.frame)
                
        def rc_value_changer(self):
                self.rc_vtk.volumeScalarOpacity.AddPoint(self.denisty_dic.get(self.rc_iso_comboBox.currentText()), self.rc_iso_slider.value()/10)
                self.rc_vtk.volumeColor.AddRGBPoint(self.denisty_dic.get(self.rc_iso_comboBox.currentText()),self.rc_red_slider.value()/10, self.rc_green_slider.value()/10, self.rc_blue_slider.value()/10)
                self.rc_vtk.renWin.update()


        def sr_value_changer(self):
                self.sro_vtk.contour.SetValue(0, self.sr_iso_slider.value())
                self.sr_iso_tbox.setPlainText(str(self.sr_iso_slider.value()))
                self.sro_vtk.actor.GetProperty().SetColor(self.sr_red_slider.value()/10, self.sr_green_slider.value()/10, self.sr_blue_slider.value()/10)
                self.sro_vtk.renWin.update()

        def setting_slider(self,set_slider,type):
                if(type == 0):
                        set_slider.setTickPosition(QSlider.TicksRight)
                        set_slider.setTickInterval(1)
                        set_slider.setSingleStep(1)
                        set_slider.setValue(1500)
                        set_slider.setMinimum(0)
                        set_slider.setMaximum(1500)
                if(type == 1):
                        set_slider.setTickPosition(QSlider.TicksRight)
                        set_slider.setTickInterval(100)
                        set_slider.setSingleStep(100)
                        set_slider.setValue(10)
                        set_slider.setMinimum(0)
                        set_slider.setMaximum(10)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "DICOM Reader"))
                self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#ffffff;\">Surface Rendering</span></p></body></html>"))
                self.sr_iso_box.setTitle(_translate("MainWindow", "Iso Value"))
                self.sr_import_box.setTitle(_translate("MainWindow", "Import DICOM files "))
                self.sr_browse.setText(_translate("MainWindow", "Browse"))
                self.sr_rgb_box.setTitle(_translate("MainWindow", "RGB Transfer function"))
                self.sr_red.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ff0000;\">RED</span></p></body></html>"))
                self.sr_blue.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#00007f;\">BLUE</span></p></body></html>"))
                self.sr_green.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#00aa00;\">GREEN</span></p></body></html>"))
                self.sr_window_box.setTitle(_translate("MainWindow", "window"))
                self.tabw.setTabText(self.tabw.indexOf(self.tab), _translate("MainWindow", "Surface Rendering"))
                self.rc_iso_box.setTitle(_translate("MainWindow", "Iso Value"))
                self.rc_iso_comboBox.setItemText(0, _translate("MainWindow", "skin1"))
                self.rc_iso_comboBox.setItemText(1, _translate("MainWindow", "skin2"))
                self.rc_iso_comboBox.setItemText(2, _translate("MainWindow", "tissue"))
                self.rc_iso_comboBox.setItemText(3, _translate("MainWindow", "bones"))
                self.rc_iso_comboBox.setItemText(4, _translate("MainWindow", "dense bones"))
                self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#ffffff;\">Ray Casting Rendering</span></p></body></html>"))
                self.rc_import_box.setTitle(_translate("MainWindow", "Import DICOM files "))
                self.rc_browse.setText(_translate("MainWindow", "Browse"))
                self.rc_rgb_box.setTitle(_translate("MainWindow", "RGB Transfer function"))
                self.rc_red.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ff0000;\">RED</span></p></body></html>"))
                self.rc_blue.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#00007f;\">BLUE</span></p></body></html>"))
                self.rc_green.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#00aa00;\">GREEN</span></p></body></html>"))
                self.rc_window_box.setTitle(_translate("MainWindow", "window"))
                self.tabw.setTabText(self.tabw.indexOf(self.tab_2), _translate("MainWindow", "Ray Casting Rendering"))



class vtk_W : 

        def __init__(self,direc_path):
                self.dirc = direc_path
                self.frame = Qt.QFrame()
                self.contour = 0
                self.load_data()
                self.renWin = 0
                
        def load_data(self):
                self.reader = vtk.vtkDICOMImageReader()
                self.reader.SetDirectoryName(self.dirc)
                self.reader.Update()
                # vtkImageData
                self.imageData = self.reader.GetOutput()
        def surface_rendering(self):
                self.contour = vtk.vtkContourFilter()
                self.contour.SetValue(0,1500) # 0.5*(minVal + maxVal))
                self.contour.SetInputData(self.imageData)
                surfaceNormals = vtk.vtkPolyDataNormals()
                surfaceNormals.SetInputConnection(self.contour.GetOutputPort())
                surfaceNormals.SetFeatureAngle(90.0)
                mapper = vtk.vtkPolyDataMapper()
                mapper.ScalarVisibilityOff()
                mapper.SetInputConnection(surfaceNormals.GetOutputPort())
                self.actor = vtk.vtkActor()
                self.actor.SetMapper(mapper)
                self.actor.GetProperty().SetColor(222/256., 184/256., 135/256.)
                self.sr_rendering()
        def ray_casting(self):
                self.volumeMapper = vtk.vtkSmartVolumeMapper()
                self.volumeMapper.SetInputData(self.imageData)
                self.volumeColor = vtk.vtkColorTransferFunction()
                self.volumeColor.AddRGBPoint(0,    0.00, 0.000, 0.00) 
                self.volumeColor.AddRGBPoint(1,    0.00, 0.000, 0.00) 
                self.volumeColor.AddRGBPoint(100,    1.00, 0.000, 0.00)   
                self.volumeColor.AddRGBPoint(500,    1.0, 1.00, 1.00)   
                self.volumeColor.AddRGBPoint(1000,   1.00, 1.00, 1.00)   
                self.volumeColor.AddRGBPoint(1500,   1.0, 1.0, 1.0) 
                self.volumeColor.AddRGBPoint(2000,   0, 0, 0)     
                
                self.volumeScalarOpacity = vtk.vtkPiecewiseFunction()

                self.volumeScalarOpacity.AddPoint(0,  0.00)
                self.volumeScalarOpacity.AddPoint(1,  0.00)
                self.volumeScalarOpacity.AddPoint(100,  1.00)
                self.volumeScalarOpacity.AddPoint(500,  1.0000)
                self.volumeScalarOpacity.AddPoint(1000, 1.000)
                self.volumeScalarOpacity.AddPoint(1500, 1.0)
                self.volumeScalarOpacity.AddPoint(2000, 0.00)

               
                volumeGradientOpacity = vtk.vtkPiecewiseFunction()

                volumeGradientOpacity.AddPoint(0,   1.0)
                volumeGradientOpacity.AddPoint(1,   1.0)
                volumeGradientOpacity.AddPoint(100,   1.0)
                volumeGradientOpacity.AddPoint(100,   1.0)
                volumeGradientOpacity.AddPoint(500, 1.0)
                volumeGradientOpacity.AddPoint(1000,  1.0)
                volumeGradientOpacity.AddPoint(1500, 1.0)

                
                volumeProperty = vtk.vtkVolumeProperty()
                volumeProperty.SetColor(self.volumeColor)
                volumeProperty.SetScalarOpacity(self.volumeScalarOpacity)
                volumeProperty.SetGradientOpacity(volumeGradientOpacity)
                volumeProperty.SetInterpolationTypeToLinear()
                volumeProperty.ShadeOn()
                
                self.volume = vtk.vtkVolume()
                self.volume.SetMapper(self.volumeMapper)
                self.volume.SetProperty(volumeProperty)
                self.rc_rendering()
                # Finally, add the volume to the renderer
              

        def sr_rendering(self):

                self.renWin = qvtk(self.frame)
                self.ren = vtk.vtkRenderer()
                self.ren.AddActor(self.actor)
                self.ren.SetBackground(0, 0, 0)
                self.renWin.GetRenderWindow().AddRenderer(self.ren)
                self.renWin.SetSize( 411, 411)

                self.iren = self.renWin.GetRenderWindow().GetInteractor()
                
        

                self.iren.Initialize()
                self.renWin.Render()
                self.iren.Start()
        def rc_rendering(self):
    
                self.renWin = qvtk(self.frame)
                self.ren = vtk.vtkRenderer()
                camera =  self.ren.GetActiveCamera()
                c = self.volume.GetCenter()
                camera.SetFocalPoint(c[0], c[1], c[2])
                camera.SetPosition(c[0] + 400, c[1], c[2])
                camera.SetViewUp(0, 0, -1)
                self.renWin.SetSize(640, 480)
                self.ren.AddViewProp(self.volume)
                self.renWin.GetRenderWindow().AddRenderer(self.ren)
                self.renWin.SetSize( 411, 411)
                self.iren = self.renWin.GetRenderWindow().GetInteractor()
                self.iren.Initialize()
                self.renWin.Render()
                self.iren.Start()





                



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DICOM = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(DICOM)
    DICOM.show()
    sys.exit(app.exec_())