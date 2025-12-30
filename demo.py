import threading
import queue

import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QGridLayout
)
from PyQt5.QtCore import QTimer

from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Timers for Hope's corner kitchen ovens")
        #self.resize(1120,660)

        self.btn_0 = QPushButton("Start")


        # ----- Central widget & main layout -----
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)

        # --- steam_top_oven ---
        steam_top_oven_layout = QHBoxLayout()
        # - init list -
        self.steam_top_oven_plus_buttons = []
        self.steam_top_oven_minus_buttons = []
        self.steam_top_oven_dish_labels = []
        self.steam_top_oven_timer_labels = []
        self.steam_top_oven_timers = []
        # - append -
        self.steam_top_oven_plus_buttons.append(QPushButton("+"))
        self.steam_top_oven_minus_buttons.append(QPushButton("-"))
        self.steam_top_oven_dish_labels.append(QLabel("EGGS"))
        self.steam_top_oven_timer_labels.append(QLabel("00:00"))
        # - connect -
        self.steam_top_oven_plus_buttons[0].clicked.connect(self.add_one_minute)
        self.steam_top_oven_minus_buttons[0].clicked.connect(self.remove_one_minute)
        # - add widget -
        steam_top_oven_layout.addWidget(self.steam_top_oven_plus_buttons[0])
        steam_top_oven_layout.addWidget(self.steam_top_oven_minus_buttons[0])
        steam_top_oven_layout.addWidget(self.steam_top_oven_dish_labels[0])
        steam_top_oven_layout.addWidget(self.steam_top_oven_timer_labels[0])

        # steam_bottom_oven
        steam_bottom_oven_layout = QHBoxLayout()
        # - init list -
        self.steam_bottom_oven_plus_buttons = []
        self.steam_bottom_oven_minus_buttons = []
        self.steam_bottom_oven_dish_labels = []
        self.steam_bottom_oven_timer_labels = []
        self.steam_bottom_oven_timers = []
        # - append -
        self.steam_bottom_oven_plus_buttons.append(QPushButton("+"))
        self.steam_bottom_oven_minus_buttons.append(QPushButton("-"))
        self.steam_bottom_oven_dish_labels.append(QLabel("EGGS"))
        self.steam_bottom_oven_timer_labels.append(QLabel("00:00"))
        # - connect -
        self.steam_bottom_oven_plus_buttons[0].clicked.connect(self.add_one_minute)
        self.steam_bottom_oven_minus_buttons[0].clicked.connect(self.remove_one_minute)
        # - add widget -
        steam_bottom_oven_layout.addWidget(self.steam_bottom_oven_plus_buttons[0])
        steam_bottom_oven_layout.addWidget(self.steam_bottom_oven_minus_buttons[0])
        steam_bottom_oven_layout.addWidget(self.steam_bottom_oven_dish_labels[0])
        steam_bottom_oven_layout.addWidget(self.steam_bottom_oven_timer_labels[0])

        # central_oven
        central_oven_layout = QHBoxLayout()
        # - init list -
        self.central_oven_plus_buttons = []
        self.central_oven_minus_buttons = []
        self.central_oven_dish_labels = []
        self.central_oven_timer_labels = []
        self.central_oven_timers = []
        # - append -
        self.central_oven_plus_buttons.append(QPushButton("+"))
        self.central_oven_minus_buttons.append(QPushButton("-"))
        self.central_oven_dish_labels.append(QLabel("EGGS"))
        self.central_oven_timer_labels.append(QLabel("00:00"))
        # - connect -
        self.central_oven_plus_buttons[0].clicked.connect(self.add_one_minute)
        self.central_oven_minus_buttons[0].clicked.connect(self.remove_one_minute)
        # - add widget -
        central_oven_layout.addWidget(self.central_oven_plus_buttons[0])
        central_oven_layout.addWidget(self.central_oven_minus_buttons[0])
        central_oven_layout.addWidget(self.central_oven_dish_labels[0])
        central_oven_layout.addWidget(self.central_oven_timer_labels[0])

        # ---- Assemble ----
        main_layout.addLayout(steam_top_oven_layout)
        main_layout.addLayout(steam_bottom_oven_layout)
        main_layout.addLayout(central_oven_layout)

    # all the initialized and opened things must be closed and terminated to exit nice
    def closeEvent(self, event):
        print("closeEvent() called")
        print("Exit app")
        event.accept() # let the window close        

    def add_one_minute(self):
        print ('self.add_one_minute')

    def remove_one_minute(self):
        print ('self.remove_one_minute')


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
