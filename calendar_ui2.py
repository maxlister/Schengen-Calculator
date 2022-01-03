# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendar2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import datetime as dt

from PyQt5 import QtCore, QtGui, QtWidgets

from CustomWidgets import ClickableLabel, CustomCalendar


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(558, 241)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 538, 151))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(6, 8, 12, 8)
        self.gridLayout.setHorizontalSpacing(12)
        self.gridLayout.setVerticalSpacing(8)
        self.gridLayout.setObjectName("gridLayout")

        self.holidays = [(dt.date(2022, 4, 11), dt.date(2022, 5, 9)),
                         (dt.date(2022, 6, 6), dt.date(2022, 7, 7)),
                         (dt.date(2022, 9, 9), dt.date(2022, 10, 20))]

        # Add Labels
        self.labels = [QtWidgets.QLabel(self.scrollAreaWidgetContents),
                       QtWidgets.QLabel(self.scrollAreaWidgetContents),
                       QtWidgets.QLabel(self.scrollAreaWidgetContents)]

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        font = QtGui.QFont()
        font.setPointSize(12)

        for idx, label in enumerate(self.labels):
            sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
            label.setSizePolicy(sizePolicy)
            label.setFont(font)
            label.setObjectName("label_{}".format(idx + 1))
            self.gridLayout.addWidget(label, 0, idx + 1, 1, 1)

        # Add flight rows
        self.flight_rows = []
        self.provisional_flights = tuple()
        self.add_row()

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        # Add flight button
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_btn.sizePolicy().hasHeightForWidth())
        self.add_btn.setSizePolicy(sizePolicy)
        self.add_btn.setObjectName("add_btn")
        self.add_btn.clicked.connect(self.add_row)
        self.verticalLayout.addWidget(self.add_btn)

        # Days label
        self.days_lbl = QtWidgets.QLabel(self.centralwidget)
        sizePolicy.setHeightForWidth(self.days_lbl.sizePolicy().hasHeightForWidth())
        self.days_lbl.setSizePolicy(sizePolicy)
        self.days_lbl.setObjectName("days_lbl")
        self.days_lbl.setText("Days used")
        self.verticalLayout.addWidget(self.days_lbl)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 558, 21))
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    @property
    def rows(self):
        return len(self.flight_rows)

    def add_row(self):
        # flight_row = [QtWidgets.QPushButton("x", self.scrollAreaWidgetContents),
        #               ClickableLineEdit(self.scrollAreaWidgetContents),
        #               ClickableLineEdit(self.scrollAreaWidgetContents),
        #               ClickableLineEdit(self.scrollAreaWidgetContents)]

        flight_row = [QtWidgets.QPushButton("x", self.scrollAreaWidgetContents),
                      ClickableLabel(self.scrollAreaWidgetContents),
                      ClickableLabel(self.scrollAreaWidgetContents),
                      ClickableLabel(self.scrollAreaWidgetContents)]

        self.flight_rows.append(flight_row)
        # Delete button
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(flight_row[0].sizePolicy().hasHeightForWidth())
        flight_row[0].setSizePolicy(sizePolicy)
        flight_row[0].setMaximumSize(QtCore.QSize(40, 16777215))
        flight_row[0].setObjectName("del_button_{}".format(self.rows))
        row_num = self.rows - 1
        flight_row[0].clicked.connect(lambda: self.delete_row(row_num))
        self.gridLayout.addWidget(flight_row[0], self.rows, 0, 1, 1)

        # Date Labels
        font = QtGui.QFont()
        font.setPointSize(10)
        for col_num, date_label in enumerate(flight_row[1::]):
            date_label.setMinimumSize(QtCore.QSize(0, 20))
            date_label.setFont(font)
            date_label.setCursor(QtCore.Qt.CursorShape.IBeamCursor)
            date_label.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            date_label.setObjectName("lineEdit_{}".format(3 * (self.rows - 1) + (col_num + 1)))
            self.gridLayout.addWidget(date_label, self.rows, col_num + 1, 1, 1)
        # Only spawn calendar on first two line edits
        flight_row[1].clicked.connect(lambda: self.spawn_calendar(flight_row[1], True))
        flight_row[2].clicked.connect(lambda: self.spawn_calendar(flight_row[2], False))

        # self.flight_rows.append(flight_row)

    def delete_row(self, row_idx):
        print(row_idx)
        entry_lbl, exit_lbl = self.flight_rows[row_idx][1:3]  # Entry and Exit Date indexes
        entry, exit = entry_lbl.text(), exit_lbl.text()
        if not entry and not exit:
            for widget in reversed(self.flight_rows[row_idx]):
                self.gridLayout.removeWidget(widget)
                widget.setParent(None)
            del self.flight_rows[row_idx]
            print(self.rows)

    def spawn_calendar(self, label, is_entry):
        def callback():
            label.setText(cal.selectedDate().toString("dd/MM/yyyy"))

            self.new_window.close()

        self.new_window = QtWidgets.QWidget()
        cal = CustomCalendar(is_entry, self.holidays, self.new_window)
        cal.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        cal.setMinimumDate(QtCore.QDate.currentDate())
        cal.clicked.connect(callback)
        layout = QtWidgets.QVBoxLayout(self.new_window)
        layout.addWidget(cal)
        self.new_window.show()

    def add_holiday(self):
        self.holidays.append(self.provisional_flights)
        self.provisional_flights = tuple()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labels[0].setText(_translate("MainWindow", "Entry Date"))
        self.labels[1].setText(_translate("MainWindow", "Exit Date"))
        self.labels[2].setText(_translate("MainWindow", "Days Stayed"))
        self.flight_rows[0][0].setText(_translate("MainWindow", "x"))
        # self.flight_rows[1][0].setText(_translate("MainWindow", "x"))
        self.add_btn.setText(_translate("MainWindow", "Add Flight"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
