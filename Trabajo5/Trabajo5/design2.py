# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide6 import QtWidgets
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QTabWidget,
    QTableView, QToolBar, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionInsertar = QAction(MainWindow)
        self.actionInsertar.setObjectName(u"actionInsertar")
        icon = QIcon()
        icon.addFile(u":/icons/database--plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionInsertar.setIcon(icon)
        self.actionModificar = QAction(MainWindow)
        self.actionModificar.setObjectName(u"actionModificar")
        icon1 = QIcon()
        icon1.addFile(u":/icons/database--arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionModificar.setIcon(icon1)
        self.actionEliminar = QAction(MainWindow)
        self.actionEliminar.setObjectName(u"actionEliminar")
        icon2 = QIcon()
        icon2.addFile(u":/icons/database--minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionEliminar.setIcon(icon2)
        self.actionGenerarInforme = QAction(MainWindow)
        self.actionGenerarInforme.setObjectName(u"actionGenerarInforme")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icono-pdf.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionGenerarInforme.setIcon(icon3)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit_ID = QLineEdit(self.groupBox)
        self.lineEdit_ID.setObjectName(u"lineEdit_ID")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_ID)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_Title = QLineEdit(self.groupBox)
        self.lineEdit_Title.setObjectName(u"lineEdit_Title")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_Title)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_2)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_3)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lineEdit_5)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_7)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabla = QTableView(self.tab)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setGeometry(QRect(0, 0, 782, 251))
        self.tabla.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Maximum)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuRegistro = QMenu(self.menubar)
        self.menuRegistro.setObjectName(u"menuRegistro")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuRegistro.menuAction())
        self.menuRegistro.addAction(self.actionInsertar)
        self.menuRegistro.addAction(self.actionModificar)
        self.menuRegistro.addAction(self.actionEliminar)
        self.toolBar.addAction(self.actionInsertar)
        self.toolBar.addAction(self.actionModificar)
        self.toolBar.addAction(self.actionEliminar)
        self.toolBar.addAction(self.actionGenerarInforme)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionInsertar.setText(QCoreApplication.translate("MainWindow", u"Insertar", None))
#if QT_CONFIG(shortcut)
        self.actionInsertar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionModificar.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
#if QT_CONFIG(shortcut)
        self.actionModificar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+M", None))
#endif // QT_CONFIG(shortcut)
        self.actionEliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
#if QT_CONFIG(shortcut)
        self.actionEliminar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.actionGenerarInforme.setText(QCoreApplication.translate("MainWindow", u"GenerarInforme", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Datos del Alumno", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Apellidos", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Curso", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Media1\u00aaEV", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Media2\u00aaEV", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Media3\u00aaEV", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.menuRegistro.setTitle(QCoreApplication.translate("MainWindow", u"Registro", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

