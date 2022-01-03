from PyQt5 import QtCore, QtWidgets, QtGui

from cal_lib import date_is_holiday


class ClickableLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()  # signal when the text entry is left-clicked

    def __init__(self, *args):
        super(ClickableLabel, self).__init__(*args)

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.clicked.emit()
        else:
            super().mouseReleaseEvent(event)


class CustomCalendar(QtWidgets.QCalendarWidget):
    def __init__(self, is_entry, holidays, *args):
        super(CustomCalendar, self).__init__(*args)
        if is_entry:
            min_date = min(QtCore.QDate(sorted(holidays)[0][1]), QtCore.QDate.currentDate())
            self.setMinimumDate(min_date)
        self.holiday_endpoints = holidays
        self.color = QtGui.QColor("gray")
        self.color.setAlpha(128)
        self.selectionChanged.connect(self.updateCells)

    def paintCell(self, painter, rect, date):
        super(CustomCalendar, self).paintCell(painter, rect, date)
        if date_is_holiday(date.toPyDate(), self.holiday_endpoints):
            painter.fillRect(rect, self.color)
