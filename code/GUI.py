from keybinds import *
from functools import partial
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QCheckBox, QSystemTrayIcon, \
    QSpacerItem, QSizePolicy, QMenu, QAction, QStyle, qApp, QPushButton, QGroupBox
from PyQt5.QtCore import QSize
from PyQt5 import QtGui


class MainWindow(QMainWindow):
    button_list = [None, None, None, None, None, None]
    hero_list = ["slark", "pudge", "legion_commander", "wraith_king", "boldak", "custom"]

    def __init__(self):
        QMainWindow.__init__(self)
        app.setStyle("Fusion")
        self.setFixedSize(QSize(600, 300))
        self.setWindowTitle("CringeSounds")
        self.setWindowIcon(QtGui.QIcon("../source/images/tray_icon.png"))

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QtGui.QIcon("../source/images/tray_icon.png"))
        self.tray_icon.activated.connect(self.showFromTray)

        show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)
        hide_action = QAction("Hide", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(qApp.quit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        central_widget = QWidget(self)
        self.grid = QGridLayout(central_widget)
        self.setCentralWidget(central_widget)

        for button_number in range(5):
            self.new_button(0, button_number, self.hero_list[button_number])

        self.new_button(1, 5, "add_more")
        self.button_list[5].clicked.connect(self.add_clicked)
        self.now_clicked = 0
        self.hero_clicked(0, self.hero_list[0])
        stereoKeyBind()

    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def showFromTray(self, reason):
        if reason == 3:
            self.show()

    def new_button(self, i, j, name):
        self.button_list[j] = QPushButton(self)
        self.button_list[j].clicked.connect(lambda: self.hero_clicked(j, name))
        self.button_list[j].setIcon(QtGui.QIcon('../source/images/{}.png'.format(name)))
        self.button_list[j].setIconSize(QSize(150, 150))
        self.button_list[j].setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        if j>4:
            col_num = j-5
        else:
            col_num = j
        self.grid.addWidget(self.button_list[j], i, col_num)

    def hero_clicked(self, j, name):
        self.button_list[self.now_clicked].setIcon(
            QtGui.QIcon('../source/images/{}.png'.format(self.hero_list[self.now_clicked])))
        self.now_clicked = j
        self.button_list[j].setIcon(QtGui.QIcon('../source/images/{}_active.png'.format(name)))
        self.button_list[j].setIcon(QtGui.QIcon('../source/images/{}_active.png'.format(name)))
        heroKeyBind(10, name)

    def add_clicked(self):
        print("add")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
