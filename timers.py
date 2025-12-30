import threading
import queue

import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QGridLayout
)
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QPixmap

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

        self.plus_buttons = []
        self.minus_buttons = []
        self.dish_labels = []
        self.timer_labels = []

        # -----------------------------
        # ----- left ovens layout -----
        # -----------------------------
        container_widget = QWidget()
        container_widget.setStyleSheet("background-color: blue;")
        main_layout.addWidget(container_widget)
        left_ovens_layout = QVBoxLayout(container_widget)

        # --- left_top_oven ---
        container_widget = QWidget()
        container_widget.setStyleSheet("background-color: white;")
        left_ovens_layout.addWidget(container_widget)
        left_top_oven_layout = QVBoxLayout(container_widget)

        left_top_oven_layout.addWidget(QLabel("TOP STEAM OVEN"))
        # - init list -
        left_top_oven_layouts = []
        for i in range (TOP_LEFT_OVEN_SPACES):
            # - append -
            left_top_oven_layouts.append(QHBoxLayout())
            self.plus_buttons.append(QPushButton("+"))
            self.plus_buttons[tray_id].tray_id = tray_id
            self.minus_buttons.append(QPushButton("-"))
            self.minus_buttons[tray_id].tray_id = tray_id
            self.dish_labels.append(QLabel("QUICHE"))
            self.timer_labels.append(QLabel("00:00"))
            # - connect -
            self.plus_buttons[tray_id].clicked.connect(self.add_one_minute)
            self.minus_buttons[tray_id].clicked.connect(self.remove_one_minute)
            # - add widget -
            left_top_oven_layouts[i].addWidget(self.plus_buttons[tray_id])
            left_top_oven_layouts[i].addWidget(self.minus_buttons[tray_id])
            left_top_oven_layouts[i].addWidget(self.dish_labels[tray_id])
            left_top_oven_layouts[i].addWidget(self.timer_labels[tray_id])
            # - assemble -
            left_top_oven_layout.addLayout(left_top_oven_layouts[i])
            tray_id+=1

        # --- left_bottom_oven ---
        container_widget = QWidget()
        container_widget.setStyleSheet("background-color: white;")
        left_ovens_layout.addWidget(container_widget)
        left_bottom_oven_layout = QVBoxLayout(container_widget)

        left_bottom_oven_layout.addWidget(QLabel("BOTTOM STEAM OVEN"))
        # - init list -
        left_bottom_oven_layouts = []
        for i in range (BOTTOM_LEFT_OVEN_SPACES):
            # - append -
            left_bottom_oven_layouts.append(QHBoxLayout())
            self.plus_buttons.append(QPushButton("+"))
            self.plus_buttons[tray_id].tray_id = tray_id
            self.minus_buttons.append(QPushButton("-"))
            self.minus_buttons[tray_id].tray_id = tray_id
            self.dish_labels.append(QLabel("QUICHE"))
            self.timer_labels.append(QLabel("00:00"))
            # - connect -
            self.plus_buttons[tray_id].clicked.connect(self.add_one_minute)
            self.minus_buttons[tray_id].clicked.connect(self.remove_one_minute)
            # - add widget -
            left_bottom_oven_layouts[i].addWidget(self.plus_buttons[tray_id])
            left_bottom_oven_layouts[i].addWidget(self.minus_buttons[tray_id])
            left_bottom_oven_layouts[i].addWidget(self.dish_labels[tray_id])
            left_bottom_oven_layouts[i].addWidget(self.timer_labels[tray_id])
            # - assemble -
            left_bottom_oven_layout.addLayout(left_bottom_oven_layouts[i])
            tray_id+=1

        # -----------------------------------
        # ----- DISHES AND CENTRAL OVEN -----
        # -----------------------------------
        container_widget = QWidget()
        container_widget.setStyleSheet("background-color: blue;")
        main_layout.addWidget(container_widget)
        dishes_and_central_oven_layout = QVBoxLayout(container_widget)

        # ----- DISHES -----
        container_widget = QWidget()
        container_widget.setStyleSheet("background-color: white;")
        dishes_and_central_oven_layout.addWidget(container_widget)
        dishes_layout = QVBoxLayout(container_widget)

        dishes_layout.addWidget(QLabel("DISHES"))

        self.dishes_buttons = []
        self.dishes_buttons.append(QPushButton("QUICHE"))
        self.dishes_buttons.append(QPushButton("BEANS"))
        self.dishes_buttons.append(QPushButton("MASHED POTATOES"))
        self.dishes_buttons.append(QPushButton("PROTEIN VEGGIE"))
        for i in range (len(self.dishes_buttons)):
            dishes_layout.addWidget(self.dishes_buttons[i])
            self.dishes_buttons[i].clicked.connect(self.selected_dish)

        # ----- central_oven -----
        central_oven_layout = QVBoxLayout()

        container_widget = QWidget()
        container_widget.setStyleSheet("background-color: white;")
        dishes_and_central_oven_layout.addWidget(container_widget)
        central_oven_layout = QVBoxLayout(container_widget)

        central_oven_layout.addWidget(QLabel("CENTRAL OVEN"))
        # - init list -
        central_oven_layouts = []
        for i in range (CENTRAL_OVEN_SPACES):
            # - append -
            central_oven_layouts.append(QHBoxLayout())
            self.plus_buttons.append(QPushButton("+"))
            self.plus_buttons[tray_id].tray_id = tray_id
            self.minus_buttons.append(QPushButton("-"))
            self.minus_buttons[tray_id].tray_id = tray_id
            self.dish_labels.append(QLabel("QUICHE"))
            self.timer_labels.append(QLabel("00:00"))
            # - connect -
            self.plus_buttons[tray_id].clicked.connect(self.add_one_minute)
            self.minus_buttons[tray_id].clicked.connect(self.remove_one_minute)
            # - add widget -
            central_oven_layouts[i].addWidget(self.plus_buttons[tray_id])
            central_oven_layouts[i].addWidget(self.minus_buttons[tray_id])
            central_oven_layouts[i].addWidget(self.dish_labels[tray_id])
            central_oven_layouts[i].addWidget(self.timer_labels[tray_id])
            # - assemble -
            central_oven_layout.addLayout(central_oven_layouts[i])
            tray_id+=1

        # ------------------------------
        # ----- right ovens layout -----
        # ------------------------------
        container_widget = QWidget()
        container_widget.setStyleSheet("background-color: blue;")
        main_layout.addWidget(container_widget)
        right_ovens_layout = QVBoxLayout(container_widget)

        # --- right_top_oven ---
        container_widget = QWidget()
        container_widget.setStyleSheet("background-color: white;")
        right_ovens_layout.addWidget(container_widget)
        right_top_oven_layout = QVBoxLayout(container_widget)

        right_top_oven_layout.addWidget(QLabel("TOP RIGHT OVEN"))
        # - init list -
        right_top_oven_layouts = []
        for i in range (TOP_RIGHT_OVEN_SPACES):
            # - append -
            right_top_oven_layouts.append(QHBoxLayout())
            self.plus_buttons.append(QPushButton("+"))
            self.plus_buttons[tray_id].tray_id = tray_id
            self.minus_buttons.append(QPushButton("-"))
            self.minus_buttons[tray_id].tray_id = tray_id
            self.dish_labels.append(QLabel("QUICHE"))
            self.timer_labels.append(QLabel("00:00"))
            # - connect -
            self.plus_buttons[tray_id].clicked.connect(self.add_one_minute)
            self.minus_buttons[tray_id].clicked.connect(self.remove_one_minute)
            # - add widget -
            right_top_oven_layouts[i].addWidget(self.plus_buttons[tray_id])
            right_top_oven_layouts[i].addWidget(self.minus_buttons[tray_id])
            right_top_oven_layouts[i].addWidget(self.dish_labels[tray_id])
            right_top_oven_layouts[i].addWidget(self.timer_labels[tray_id])
            # - assemble -
            right_top_oven_layout.addLayout(right_top_oven_layouts[i])
            tray_id+=1

        # right_bottom_oven
        container_widget = QWidget()
        container_widget.setStyleSheet("background-color: white;")
        right_ovens_layout.addWidget(container_widget)
        right_bottom_oven_layout = QVBoxLayout(container_widget)

        right_bottom_oven_layout.addWidget(QLabel("BOTTOM RIGHT OVEN"))
        # - init list -
        right_bottom_oven_layouts = []

        for i in range (BOTTOM_RIGHT_OVEN_SPACES):
            # - append -
            right_bottom_oven_layouts.append(QHBoxLayout())
            self.plus_buttons.append(QPushButton("+"))
            self.plus_buttons[tray_id].tray_id = tray_id
            self.minus_buttons.append(QPushButton("-"))
            self.minus_buttons[tray_id].tray_id = tray_id
            self.dish_labels.append(QLabel("QUICHE"))
            self.timer_labels.append(QLabel("00:00"))
            # - connect -
            self.plus_buttons[tray_id].clicked.connect(self.add_one_minute)
            self.minus_buttons[tray_id].clicked.connect(self.remove_one_minute)
            # - add widget -
            right_bottom_oven_layouts[i].addWidget(self.plus_buttons[tray_id])
            right_bottom_oven_layouts[i].addWidget(self.minus_buttons[tray_id])
            right_bottom_oven_layouts[i].addWidget(self.dish_labels[tray_id])
            right_bottom_oven_layouts[i].addWidget(self.timer_labels[tray_id])
            # - assemble -
            right_bottom_oven_layout.addLayout(right_bottom_oven_layouts[i])
            tray_id+=1


    # all the initialized and opened things must be closed and terminated to exit nice
    def closeEvent(self, event):
        print("closeEvent() called")
        print("Exit app")
        event.accept() # let the window close

    def add_one_minute(self):
        print (self.sender().tray_id)
        print (self.sender().text())

    def remove_one_minute(self):
        print (self.sender().tray_id)
        print (self.sender().text())

    def selected_dish(self):
        print (self.sender().text())


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
