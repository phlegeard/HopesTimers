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
        #self.resize(600,200)

        # ----- Main layout -----
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QHBoxLayout(central)

        # ----- left oven layout -----
        left_ovens_layout = QVBoxLayout(central)

        # --- left_top_oven ---
        left_top_oven_layout = QHBoxLayout()
        # - init list -
        self.left_top_oven_plus_buttons = []
        self.left_top_oven_minus_buttons = []
        self.left_top_oven_dish_labels = []
        self.left_top_oven_timer_labels = []
        self.left_top_oven_timers = []
        for i in range (1):
            # - append -
            self.left_top_oven_plus_buttons.append(QPushButton("1,+"))
            self.left_top_oven_minus_buttons.append(QPushButton("1,-"))
            self.left_top_oven_dish_labels.append(QLabel("1,EGGS"))
            self.left_top_oven_timer_labels.append(QLabel("1,00:00"))
            # - connect -
            self.left_top_oven_plus_buttons[i].clicked.connect(self.add_one_minute)
            self.left_top_oven_minus_buttons[i].clicked.connect(self.remove_one_minute)
            # - add widget -
            left_top_oven_layout.addWidget(self.left_top_oven_plus_buttons[i])
            left_top_oven_layout.addWidget(self.left_top_oven_minus_buttons[i])
            left_top_oven_layout.addWidget(self.left_top_oven_dish_labels[i])
            left_top_oven_layout.addWidget(self.left_top_oven_timer_labels[i])

        # left_bottom_oven
        left_bottom_oven_layout = QHBoxLayout()
        # - init list -
        self.left_bottom_oven_plus_buttons = []
        self.left_bottom_oven_minus_buttons = []
        self.left_bottom_oven_dish_labels = []
        self.left_bottom_oven_timer_labels = []
        self.left_bottom_oven_timers = []

        for i in range (1):
            # - append -
            self.left_bottom_oven_plus_buttons.append(QPushButton("2,+"))
            self.left_bottom_oven_minus_buttons.append(QPushButton("2,-"))
            self.left_bottom_oven_dish_labels.append(QLabel("2,EGGS"))
            self.left_bottom_oven_timer_labels.append(QLabel("2,00:00"))
            # - connect -
            self.left_bottom_oven_plus_buttons[i].clicked.connect(self.add_one_minute)
            self.left_bottom_oven_minus_buttons[i].clicked.connect(self.remove_one_minute)
            # - add widget -
            left_bottom_oven_layout.addWidget(self.left_bottom_oven_plus_buttons[i])
            left_bottom_oven_layout.addWidget(self.left_bottom_oven_minus_buttons[i])
            left_bottom_oven_layout.addWidget(self.left_bottom_oven_dish_labels[i])
            left_bottom_oven_layout.addWidget(self.left_bottom_oven_timer_labels[i])

        # - Assemble -
        left_ovens_layout.addLayout(left_top_oven_layout)
        left_ovens_layout.addLayout(left_bottom_oven_layout)

        # ----- central_oven -----
        central_oven_layout = QHBoxLayout()
        # - init list -
        self.central_oven_plus_buttons = []
        self.central_oven_minus_buttons = []
        self.central_oven_dish_labels = []
        self.central_oven_timer_labels = []
        self.central_oven_timers = []

        for i in range (1):
            # - append -
            self.central_oven_plus_buttons.append(QPushButton("3,+"))
            self.central_oven_minus_buttons.append(QPushButton("3,-"))
            self.central_oven_dish_labels.append(QLabel("3,EGGS"))
            self.central_oven_timer_labels.append(QLabel("3,00:00"))
            # - connect -
            self.central_oven_plus_buttons[i].clicked.connect(self.add_one_minute)
            self.central_oven_minus_buttons[i].clicked.connect(self.remove_one_minute)
            # - add widget -
            central_oven_layout.addWidget(self.central_oven_plus_buttons[i])
            central_oven_layout.addWidget(self.central_oven_minus_buttons[i])
            central_oven_layout.addWidget(self.central_oven_dish_labels[i])
            central_oven_layout.addWidget(self.central_oven_timer_labels[i])


        # ----- right oven layout -----
        right_ovens_layout = QVBoxLayout(central)

        # --- right_top_oven ---
        right_top_oven_layout = QHBoxLayout()
        # - init list -
        self.right_top_oven_plus_buttons = []
        self.right_top_oven_minus_buttons = []
        self.right_top_oven_dish_labels = []
        self.right_top_oven_timer_labels = []
        self.right_top_oven_timers = []
        for i in range (1):
            # - append -
            self.right_top_oven_plus_buttons.append(QPushButton("4,+"))
            self.right_top_oven_minus_buttons.append(QPushButton("4,-"))
            self.right_top_oven_dish_labels.append(QLabel("4,EGGS"))
            self.right_top_oven_timer_labels.append(QLabel("4,00:00"))
            # - connect -
            self.right_top_oven_plus_buttons[i].clicked.connect(self.add_one_minute)
            self.right_top_oven_minus_buttons[i].clicked.connect(self.remove_one_minute)
            # - add widget -
            right_top_oven_layout.addWidget(self.right_top_oven_plus_buttons[i])
            right_top_oven_layout.addWidget(self.right_top_oven_minus_buttons[i])
            right_top_oven_layout.addWidget(self.right_top_oven_dish_labels[i])
            right_top_oven_layout.addWidget(self.right_top_oven_timer_labels[i])

        # right_bottom_oven
        right_bottom_oven_layout = QHBoxLayout()
        # - init list -
        self.right_bottom_oven_plus_buttons = []
        self.right_bottom_oven_minus_buttons = []
        self.right_bottom_oven_dish_labels = []
        self.right_bottom_oven_timer_labels = []
        self.right_bottom_oven_timers = []

        for i in range (1):
            # - append -
            self.right_bottom_oven_plus_buttons.append(QPushButton("5,+"))
            self.right_bottom_oven_minus_buttons.append(QPushButton("5,-"))
            self.right_bottom_oven_dish_labels.append(QLabel("5,EGGS"))
            self.right_bottom_oven_timer_labels.append(QLabel("5,00:00"))
            # - connect -
            self.right_bottom_oven_plus_buttons[i].clicked.connect(self.add_one_minute)
            self.right_bottom_oven_minus_buttons[i].clicked.connect(self.remove_one_minute)
            # - add widget -
            right_bottom_oven_layout.addWidget(self.right_bottom_oven_plus_buttons[i])
            right_bottom_oven_layout.addWidget(self.right_bottom_oven_minus_buttons[i])
            right_bottom_oven_layout.addWidget(self.right_bottom_oven_dish_labels[i])
            right_bottom_oven_layout.addWidget(self.right_bottom_oven_timer_labels[i])

        # - Assemble -
        right_ovens_layout.addLayout(right_top_oven_layout)
        right_ovens_layout.addLayout(right_bottom_oven_layout)

        # ---- Assemble ----
        main_layout.addLayout(left_ovens_layout)
        main_layout.addLayout(central_oven_layout)
        main_layout.addLayout(right_ovens_layout)


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
