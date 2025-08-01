# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(256, 278)
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.length_doubleSpinBox = QDoubleSpinBox(self.centralwidget)
        self.length_doubleSpinBox.setObjectName(u"length_doubleSpinBox")
        self.length_doubleSpinBox.setValue(2.000000000000000)

        self.gridLayout.addWidget(self.length_doubleSpinBox, 0, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.width_doubleSpinBox = QDoubleSpinBox(self.centralwidget)
        self.width_doubleSpinBox.setObjectName(u"width_doubleSpinBox")
        self.width_doubleSpinBox.setValue(3.000000000000000)

        self.gridLayout.addWidget(self.width_doubleSpinBox, 1, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.height_doubleSpinBox = QDoubleSpinBox(self.centralwidget)
        self.height_doubleSpinBox.setObjectName(u"height_doubleSpinBox")
        self.height_doubleSpinBox.setValue(0.500000000000000)

        self.gridLayout.addWidget(self.height_doubleSpinBox, 2, 1, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.radius_doubleSpinBox = QDoubleSpinBox(self.centralwidget)
        self.radius_doubleSpinBox.setObjectName(u"radius_doubleSpinBox")
        self.radius_doubleSpinBox.setValue(0.500000000000000)

        self.gridLayout.addWidget(self.radius_doubleSpinBox, 3, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.pushButton_2)


        self.gridLayout_2.addLayout(self.verticalLayout, 2, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 256, 22))
        main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"\u0413\u043b\u0430\u0432\u043d\u043e\u0435 \u043e\u043a\u043d\u043e \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("main_window", u"\u0421\u0442\u0440\u043e\u0438\u043c \u043f\u0430\u0440\u0430\u043b\u043b\u0435\u043b\u0435\u043f\u0438\u043f\u0435\u0434 \u0441 \u043e\u0442\u0432\u0435\u0440\u0441\u0442\u0438\u0435\u043c", None))
        self.label_4.setText(QCoreApplication.translate("main_window", u"\u0414\u043b\u0438\u043d\u0430", None))
        self.label_2.setText(QCoreApplication.translate("main_window", u"\u0428\u0438\u0440\u0438\u043d\u0430", None))
        self.label_3.setText(QCoreApplication.translate("main_window", u"\u0412\u044b\u0441\u043e\u0442\u0430", None))
        self.label_5.setText(QCoreApplication.translate("main_window", u"\u041e\u0442\u0432\u0435\u0440\u0441\u0442\u0438\u0435, \u0440\u0430\u0434\u0438\u0443\u0441", None))
        self.pushButton.setText(QCoreApplication.translate("main_window", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043c\u043e\u0434\u0435\u043b\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("main_window", u"\u041f\u0440\u0435\u0434\u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u043c\u043e\u0434\u0435\u043b\u0438", None))
    # retranslateUi

