import threading
import queue

import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QGridLayout
)
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap

TOP_LEFT_OVEN_SPACES=5
BOTTOM_LEFT_OVEN_SPACES=5
CENTRAL_OVEN_SPACES=4
TOP_RIGHT_OVEN_SPACES=5
BOTTOM_RIGHT_OVEN_SPACES=5

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Timers for Hope's corner kitchen ovens")
        #self.resize(600,200)

        tray_id=0

        # ------ Main layout -------
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QHBoxLayout(central)

        # -----------------------------
        # ----- left ovens layout -----
        # -----------------------------
        container_widget = QWidget()
        container_widget.setStyleSheet("background-color: white;")
        main_layout.addWidget(container_widget)
        left_ovens_layout = QVBoxLayout(container_widget)

        # --- left_top_oven ---
        left_top_oven_layout = QVBoxLayout()
        left_top_oven_layout.addWidget(QLabel("TOP STEAM OVEN"))
        # - init list -
        left_top_oven_layouts = []
        self.left_top_oven_plus_buttons = []
        self.left_top_oven_minus_buttons = []
        self.left_top_oven_dish_labels = []
        self.left_top_oven_timer_labels = []
        self.left_top_oven_timers = []
        for i in range (TOP_LEFT_OVEN_SPACES):
            # - append -
            left_top_oven_layouts.append(QHBoxLayout())
            self.left_top_oven_plus_buttons.append(QPushButton("+"))
            self.left_top_oven_plus_buttons[i].tray_id = tray_id
            self.left_top_oven_minus_buttons.append(QPushButton("-"))
            self.left_top_oven_minus_buttons[i].tray_id = tray_id
            self.left_top_oven_dish_labels.append(QLabel("EGGS"))
            self.left_top_oven_timer_labels.append(QLabel("00:00"))
            # - connect -
            self.left_top_oven_plus_buttons[i].clicked.connect(self.add_one_minute)
            self.left_top_oven_minus_buttons[i].clicked.connect(self.remove_one_minute)
            # - add widget -
            left_top_oven_layouts[i].addWidget(self.left_top_oven_plus_buttons[i])
            left_top_oven_layouts[i].addWidget(self.left_top_oven_minus_buttons[i])
            left_top_oven_layouts[i].addWidget(self.left_top_oven_dish_labels[i])
            left_top_oven_layouts[i].addWidget(self.left_top_oven_timer_labels[i])
            # - assemble -
            left_top_oven_layout.addLayout(left_top_oven_layouts[i])
            tray_id+=1

        # --- left_bottom_oven ---
        left_bottom_oven_layout = QVBoxLayout()
        left_bottom_oven_layout.addWidget(QLabel("BOTTOM STEAM OVEN"))
        # - init list -
        left_bottom_oven_layouts = []
        self.left_bottom_oven_plus_buttons = []
        self.left_bottom_oven_minus_buttons = []
        self.left_bottom_oven_dish_labels = []
        self.left_bottom_oven_timer_labels = []
        self.left_bottom_oven_timers = []
        for i in range (BOTTOM_LEFT_OVEN_SPACES):
            # - append -
            left_bottom_oven_layouts.append(QHBoxLayout())
            self.left_bottom_oven_plus_buttons.append(QPushButton("+"))
            self.left_bottom_oven_plus_buttons[i].tray_id = tray_id
            self.left_bottom_oven_minus_buttons.append(QPushButton("-"))
            self.left_bottom_oven_minus_buttons[i].tray_id = tray_id
            self.left_bottom_oven_dish_labels.append(QLabel("EGGS"))
            self.left_bottom_oven_timer_labels.append(QLabel("00:00"))
            # - connect -
            self.left_bottom_oven_plus_buttons[i].clicked.connect(self.add_one_minute)
            self.left_bottom_oven_minus_buttons[i].clicked.connect(self.remove_one_minute)
            # - add widget -
            left_bottom_oven_layouts[i].addWidget(self.left_bottom_oven_plus_buttons[i])
            left_bottom_oven_layouts[i].addWidget(self.left_bottom_oven_minus_buttons[i])
            left_bottom_oven_layouts[i].addWidget(self.left_bottom_oven_dish_labels[i])
            left_bottom_oven_layouts[i].addWidget(self.left_bottom_oven_timer_labels[i])
            # - assemble -
            left_bottom_oven_layout.addLayout(left_bottom_oven_layouts[i])
            tray_id+=1

        # - Assemble -
        left_ovens_layout.addLayout(left_top_oven_layout)
        left_ovens_layout.addLayout(left_bottom_oven_layout)

        # ------------------------------
        # ----- central_oven -----
        # ------------------------------
        container_widget = QWidget()
        container_widget.setStyleSheet("background-color: white;")
        main_layout.addWidget(container_widget)
        central_oven_layout = QVBoxLayout(container_widget)
        central_oven_layout.addWidget(QLabel("CENTRAL OVEN"))
        # - init list -
        central_oven_layouts = []
        self.central_oven_plus_buttons = []
        self.central_oven_minus_buttons = []
        self.central_oven_dish_labels = []
        self.central_oven_timer_labels = []
        self.central_oven_timers = []

        for i in range (CENTRAL_OVEN_SPACES):
            # - append -
            central_oven_layouts.append(QHBoxLayout())
            self.central_oven_plus_buttons.append(QPushButton("+"))
            self.central_oven_plus_buttons[i].tray_id = tray_id
            self.central_oven_minus_buttons.append(QPushButton("-"))
            self.central_oven_minus_buttons[i].tray_id = tray_id
            self.central_oven_dish_labels.append(QLabel("EGGS"))
            self.central_oven_timer_labels.append(QLabel("00:00"))
            # - connect -
            self.central_oven_plus_buttons[i].clicked.connect(self.add_one_minute)
            self.central_oven_minus_buttons[i].clicked.connect(self.remove_one_minute)
            # - add widget -
            central_oven_layouts[i].addWidget(self.central_oven_plus_buttons[i])
            central_oven_layouts[i].addWidget(self.central_oven_minus_buttons[i])
            central_oven_layouts[i].addWidget(self.central_oven_dish_labels[i])
            central_oven_layouts[i].addWidget(self.central_oven_timer_labels[i])
            # - assemble -
            central_oven_layout.addLayout(central_oven_layouts[i])
            tray_id+=1

        # ------------------------------
        # ----- right ovens layout -----
        # ------------------------------
        container_widget = QWidget()
        container_widget.setStyleSheet("background-color: white;")
        main_layout.addWidget(container_widget)
        right_ovens_layout = QVBoxLayout(container_widget)

        # --- right_top_oven ---
        right_top_oven_layout = QVBoxLayout()
        right_top_oven_layout.addWidget(QLabel("TOP RIGHT OVEN"))
        # - init list -
        right_top_oven_layouts = []
        self.right_top_oven_plus_buttons = []
        self.right_top_oven_minus_buttons = []
        self.right_top_oven_dish_labels = []
        self.right_top_oven_timer_labels = []
        self.right_top_oven_timers = []
        for i in range (TOP_RIGHT_OVEN_SPACES):
            # - append -
            right_top_oven_layouts.append(QHBoxLayout())
            self.right_top_oven_plus_buttons.append(QPushButton("+"))
            self.right_top_oven_plus_buttons[i].tray_id = tray_id
            self.right_top_oven_minus_buttons.append(QPushButton("-"))
            self.right_top_oven_minus_buttons[i].tray_id = tray_id
            self.right_top_oven_dish_labels.append(QLabel("EGGS"))
            self.right_top_oven_timer_labels.append(QLabel("00:00"))
            # - connect -
            self.right_top_oven_plus_buttons[i].clicked.connect(self.add_one_minute)
            self.right_top_oven_minus_buttons[i].clicked.connect(self.remove_one_minute)
            # - add widget -
            right_top_oven_layouts[i].addWidget(self.right_top_oven_plus_buttons[i])
            right_top_oven_layouts[i].addWidget(self.right_top_oven_minus_buttons[i])
            right_top_oven_layouts[i].addWidget(self.right_top_oven_dish_labels[i])
            right_top_oven_layouts[i].addWidget(self.right_top_oven_timer_labels[i])
            # - assemble -
            right_top_oven_layout.addLayout(right_top_oven_layouts[i])
            tray_id+=1

        # right_bottom_oven
        right_bottom_oven_layout = QVBoxLayout()
        right_bottom_oven_layout.addWidget(QLabel("BOTTOM RIGHT OVEN"))
        # - init list -
        right_bottom_oven_layouts = []
        self.right_bottom_oven_plus_buttons = []
        self.right_bottom_oven_minus_buttons = []
        self.right_bottom_oven_dish_labels = []
        self.right_bottom_oven_timer_labels = []
        self.right_bottom_oven_timers = []

        for i in range (BOTTOM_RIGHT_OVEN_SPACES):
            # - append -
            right_bottom_oven_layouts.append(QHBoxLayout())
            self.right_bottom_oven_plus_buttons.append(QPushButton("+"))
            self.right_bottom_oven_plus_buttons[i].tray_id = tray_id
            self.right_bottom_oven_minus_buttons.append(QPushButton("-"))
            self.right_bottom_oven_minus_buttons[i].tray_id = tray_id
            self.right_bottom_oven_dish_labels.append(QLabel("EGGS"))
            self.right_bottom_oven_timer_labels.append(QLabel("00:00"))
            # - connect -
            self.right_bottom_oven_plus_buttons[i].clicked.connect(self.add_one_minute)
            self.right_bottom_oven_minus_buttons[i].clicked.connect(self.remove_one_minute)
            # - add widget -
            right_bottom_oven_layouts[i].addWidget(self.right_bottom_oven_plus_buttons[i])
            right_bottom_oven_layouts[i].addWidget(self.right_bottom_oven_minus_buttons[i])
            right_bottom_oven_layouts[i].addWidget(self.right_bottom_oven_dish_labels[i])
            right_bottom_oven_layouts[i].addWidget(self.right_bottom_oven_timer_labels[i])
            # - assemble -
            right_bottom_oven_layout.addLayout(right_bottom_oven_layouts[i])
            tray_id+=1

        # - Assemble -
        right_ovens_layout.addLayout(right_top_oven_layout)
        right_ovens_layout.addLayout(right_bottom_oven_layout)


    # all the initialized and opened things must be closed and terminated to exit nice
    def closeEvent(self, event):
        print("closeEvent() called")
        print("Exit app")
        event.accept() # let the window close

    def add_one_minute(self):
        print (self.sender().tray_id)

    def remove_one_minute(self):
        print (self.sender().tray_id)


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
