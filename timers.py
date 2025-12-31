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
EMPTY="     "
WIDGET_STYLE_BLUE="background-color: blue;font-size: 20px"
WIDGET_STYLE_WHITE="background-color: white;font-size: 20px"

DISHES = (\
    "QUICHE", \
    "BEANS", \
    "HASH BROWN", \
    "RICE", \
    "POTATOES", \
    "VEG. PROT.")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Timers for Hope's corner kitchen ovens")
        #self.resize(600,200)
        tray_id=0
        self.selected_dish = EMPTY
        # ----- timer ----
        # Initialize the QTimer
        self.timer = QTimer(self)
        # Connect the timeout signal to the update_time function
        self.timer.timeout.connect(self.update_time)
        # Start the timer with a 1000ms (1 second) interval
        self.timer.start(1000)

        # ------ Main layout -------
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QHBoxLayout(central)

        self.start_buttons = []
        self.cancel_buttons = []
        self.dish_labels = []
        self.timer_labels = []
        self.timer_in_seconds = []
        self.timer_active = []

        # -----------------------------
        # ----- left ovens layout -----
        # -----------------------------
        container_widget = QWidget()
        container_widget.setStyleSheet(WIDGET_STYLE_BLUE)
        main_layout.addWidget(container_widget)
        left_ovens_layout = QVBoxLayout(container_widget)

        # --- left_top_oven ---
        container_widget = QWidget()
        container_widget.setStyleSheet("background-color: white;")
        container_widget.setStyleSheet(WIDGET_STYLE_WHITE)
        left_ovens_layout.addWidget(container_widget)
        left_top_oven_layout = QVBoxLayout(container_widget)

        left_top_oven_layout.addWidget(QLabel("TOP STEAM OVEN"))
        # - init list -
        left_top_oven_layouts = []
        for i in range (TOP_LEFT_OVEN_SPACES):
            # - append -
            left_top_oven_layouts.append(QHBoxLayout())
            self.start_buttons.append(QPushButton("start"))
            self.start_buttons[tray_id].tray_id = tray_id
            self.cancel_buttons.append(QPushButton("x"))
            self.cancel_buttons[tray_id].tray_id = tray_id
            self.dish_labels.append(QLabel(EMPTY))
            self.timer_labels.append(QLabel("00:00"))
            self.timer_in_seconds.append(0)
            self.timer_active.append(0)
            # - connect -
            self.start_buttons[tray_id].clicked.connect(self.start_timer)
            self.cancel_buttons[tray_id].clicked.connect(self.cancel_timer)
            # - add widget -
            left_top_oven_layouts[i].addWidget(self.start_buttons[tray_id])
            left_top_oven_layouts[i].addWidget(self.cancel_buttons[tray_id])
            left_top_oven_layouts[i].addWidget(self.timer_labels[tray_id])
            left_top_oven_layouts[i].addWidget(self.dish_labels[tray_id])
            # - assemble -
            left_top_oven_layout.addLayout(left_top_oven_layouts[i])
            tray_id+=1

        # --- left_bottom_oven ---
        container_widget = QWidget()
        container_widget.setStyleSheet("background-color: white;")
        container_widget.setStyleSheet(WIDGET_STYLE_WHITE)
        left_ovens_layout.addWidget(container_widget)
        left_bottom_oven_layout = QVBoxLayout(container_widget)

        left_bottom_oven_layout.addWidget(QLabel("BOTTOM STEAM OVEN"))
        # - init list -
        left_bottom_oven_layouts = []
        for i in range (BOTTOM_LEFT_OVEN_SPACES):
            # - append -
            left_bottom_oven_layouts.append(QHBoxLayout())
            self.start_buttons.append(QPushButton("start"))
            self.start_buttons[tray_id].tray_id = tray_id
            self.cancel_buttons.append(QPushButton("x"))
            self.cancel_buttons[tray_id].tray_id = tray_id
            self.dish_labels.append(QLabel(EMPTY))
            self.timer_labels.append(QLabel("00:00"))
            self.timer_in_seconds.append(0)
            self.timer_active.append(0)
            # - connect -
            self.start_buttons[tray_id].clicked.connect(self.start_timer)
            self.cancel_buttons[tray_id].clicked.connect(self.cancel_timer)
            # - add widget -
            left_bottom_oven_layouts[i].addWidget(self.start_buttons[tray_id])
            left_bottom_oven_layouts[i].addWidget(self.cancel_buttons[tray_id])
            left_bottom_oven_layouts[i].addWidget(self.timer_labels[tray_id])
            left_bottom_oven_layouts[i].addWidget(self.dish_labels[tray_id])
            # - assemble -
            left_bottom_oven_layout.addLayout(left_bottom_oven_layouts[i])
            tray_id+=1

        # -----------------------------------
        # ----- DISHES AND CENTRAL OVEN -----
        # -----------------------------------
        container_widget = QWidget()
        container_widget.setStyleSheet(WIDGET_STYLE_BLUE)
        main_layout.addWidget(container_widget)
        dishes_and_central_oven_layout = QVBoxLayout(container_widget)

        # ----- DISHES -----
        container_widget = QWidget()
        container_widget.setStyleSheet(WIDGET_STYLE_WHITE)
        dishes_and_central_oven_layout.addWidget(container_widget)
        dishes_layout = QVBoxLayout(container_widget)
        dishes_layout.addWidget(QLabel("DISHES"))

        self.dishes_buttons = []
        for i in range (len(DISHES)):
            self.dishes_buttons.append(QPushButton(DISHES[i]))
            dishes_layout.addWidget(self.dishes_buttons[i])
            self.dishes_buttons[i].clicked.connect(self.select_dish)

        # ----- central_oven -----
        central_oven_layout = QVBoxLayout()

        container_widget = QWidget()
        container_widget.setStyleSheet(WIDGET_STYLE_WHITE)
        dishes_and_central_oven_layout.addWidget(container_widget)
        central_oven_layout = QVBoxLayout(container_widget)

        central_oven_layout.addWidget(QLabel("CENTRAL OVEN"))
        # - init list -
        central_oven_layouts = []
        for i in range (CENTRAL_OVEN_SPACES):
            # - append -
            central_oven_layouts.append(QHBoxLayout())
            for j in range(2):
                self.start_buttons.append(QPushButton("start"))
                self.start_buttons[tray_id].tray_id = tray_id
                self.cancel_buttons.append(QPushButton("x"))
                self.cancel_buttons[tray_id].tray_id = tray_id
                self.dish_labels.append(QLabel(EMPTY))
                self.timer_labels.append(QLabel("00:00"))
                self.timer_in_seconds.append(0)
                self.timer_active.append(0)
                # - connect -
                self.start_buttons[tray_id].clicked.connect(self.start_timer)
                self.cancel_buttons[tray_id].clicked.connect(self.cancel_timer)
                # - add widget -
                central_oven_layouts[i].addWidget(self.start_buttons[tray_id])
                central_oven_layouts[i].addWidget(self.cancel_buttons[tray_id])
                central_oven_layouts[i].addWidget(self.timer_labels[tray_id])
                central_oven_layouts[i].addWidget(self.dish_labels[tray_id])
                tray_id+=1
            # - assemble -
            central_oven_layout.addLayout(central_oven_layouts[i])

        # ------------------------------
        # ----- right ovens layout -----
        # ------------------------------
        container_widget = QWidget()
        container_widget.setStyleSheet(WIDGET_STYLE_BLUE)
        main_layout.addWidget(container_widget)
        right_ovens_layout = QVBoxLayout(container_widget)

        # --- right_top_oven ---
        container_widget = QWidget()
        container_widget.setStyleSheet(WIDGET_STYLE_WHITE)
        right_ovens_layout.addWidget(container_widget)
        right_top_oven_layout = QVBoxLayout(container_widget)

        right_top_oven_layout.addWidget(QLabel("TOP RIGHT OVEN"))
        # - init list -
        right_top_oven_layouts = []
        for i in range (TOP_RIGHT_OVEN_SPACES):
            # - append -
            right_top_oven_layouts.append(QHBoxLayout())
            for j in range(2):
                self.start_buttons.append(QPushButton("start"))
                self.start_buttons[tray_id].tray_id = tray_id
                self.cancel_buttons.append(QPushButton("x"))
                self.cancel_buttons[tray_id].tray_id = tray_id
                self.dish_labels.append(QLabel(EMPTY))
                self.timer_labels.append(QLabel("00:00"))
                self.timer_in_seconds.append(0)
                self.timer_active.append(0)
                # - connect -
                self.start_buttons[tray_id].clicked.connect(self.start_timer)
                self.cancel_buttons[tray_id].clicked.connect(self.cancel_timer)
                # - add widget -
                right_top_oven_layouts[i].addWidget(self.start_buttons[tray_id])
                right_top_oven_layouts[i].addWidget(self.cancel_buttons[tray_id])
                right_top_oven_layouts[i].addWidget(self.timer_labels[tray_id])
                right_top_oven_layouts[i].addWidget(self.dish_labels[tray_id])
                tray_id+=1
            # - assemble -
            right_top_oven_layout.addLayout(right_top_oven_layouts[i])

        # right_bottom_oven
        container_widget = QWidget()
        container_widget.setStyleSheet(WIDGET_STYLE_WHITE)
        right_ovens_layout.addWidget(container_widget)
        right_bottom_oven_layout = QVBoxLayout(container_widget)

        right_bottom_oven_layout.addWidget(QLabel("BOTTOM RIGHT OVEN"))
        # - init list -
        right_bottom_oven_layouts = []

        for i in range (BOTTOM_RIGHT_OVEN_SPACES):
            # - append -
            right_bottom_oven_layouts.append(QHBoxLayout())
            for j in range(2):
                self.start_buttons.append(QPushButton("start"))
                self.start_buttons[tray_id].tray_id = tray_id
                self.cancel_buttons.append(QPushButton("x"))
                self.cancel_buttons[tray_id].tray_id = tray_id
                self.dish_labels.append(QLabel(EMPTY))
                self.timer_labels.append(QLabel("00:00"))
                self.timer_in_seconds.append(0)
                self.timer_active.append(0)
                # - connect -
                self.start_buttons[tray_id].clicked.connect(self.start_timer)
                self.cancel_buttons[tray_id].clicked.connect(self.cancel_timer)
                # - add widget -
                right_bottom_oven_layouts[i].addWidget(self.start_buttons[tray_id])
                right_bottom_oven_layouts[i].addWidget(self.cancel_buttons[tray_id])
                right_bottom_oven_layouts[i].addWidget(self.timer_labels[tray_id])
                right_bottom_oven_layouts[i].addWidget(self.dish_labels[tray_id])
                tray_id+=1
            # - assemble -
            right_bottom_oven_layout.addLayout(right_bottom_oven_layouts[i])


    # all the initialized and opened things must be closed and terminated to exit nice
    def closeEvent(self, event):
        print("closeEvent() called")
        print("Exit app")
        event.accept() # let the window close

    def start_timer(self):
        if self.selected_dish is not EMPTY:
            tray_id=self.sender().tray_id
            self.dish_labels[tray_id].setText(self.selected_dish)
            self.timer_active[tray_id] = 1
        #print (self.sender().tray_id)
        #print (self.sender().text())

    def cancel_timer(self):
        tray_id=self.sender().tray_id
        self.dish_labels[tray_id].setText(EMPTY)
        self.timer_active[tray_id] = 0
        self.timer_in_seconds[tray_id]=0
        #print (self.sender().tray_id)
        #print (self.sender().text())

    def select_dish(self):
        self.selected_dish=self.sender().text()
        #print(self.sender().text())
        for i in range (len(self.dishes_buttons)):
            #print(self.dishes_buttons[i].text())
            if  (self.sender().text() == self.dishes_buttons[i].text()):
                self.dishes_buttons[i].setStyleSheet("background-color: green;")
            else:
                self.dishes_buttons[i].setStyleSheet("background-color: white;")

    def update_time(self):
        #print("timer called")
        for i in range(len(self.timer_in_seconds)):
            if self.timer_active[i]==1:
                 self.timer_in_seconds[i] += 1
            mins, secs = divmod(self.timer_in_seconds[i], 60)
            timer_display = f'{mins:02}:{secs:02}'
            self.timer_labels[i].setText(timer_display)


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
