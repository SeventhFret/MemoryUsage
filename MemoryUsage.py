from PySide6.QtCore import QThread, QTimer
from PySide6.QtWidgets import QLabel, QPushButton, QProgressBar, QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget
from PySide6.QtGui import Qt, QFont
from os import system
import pyqtgraph as pg
import sys
import psutil


system('clear')


class MemoryUsage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mem_data = psutil.virtual_memory()
        self.initUI()


    def initUI(self):
        # self.setFixedSize(600, 600)
        self.setUpdatesEnabled(True)
        self.resize(600, 600)
        self.setWindowTitle('Memory Usage')
        self.setStyleSheet('''background-color: black;''')

        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)

        self.font40 = QFont("Georgia", 40, 700)
        self.font25 = QFont("Georgia", 25, 700)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.setAlignment(Qt.AlignCenter)


        self.firstLineLayout = QHBoxLayout()
        # self.setCentralWidget(self.mainLayout)

        self.appTitle = QLabel(text='Memory Usage Program')
        self.appTitle.setFont(self.font40)

        self.firstLineText = QLabel('Total Memory:')
        self.firstLineText.setFont(self.font25)
        self.firstLineText.setStyleSheet('''color: maroon;
margin-top: 20%''')

        self.firstLineText2 = QLabel(str(self.mem_data.total // 1024 ** 3) + " Gb")
        self.firstLineText2.setFont(self.font25)

        self.firstLineLayout.addWidget(self.firstLineText)
        self.firstLineLayout.addWidget(self.firstLineText2)
        
        pen = pg.mkPen(color=(255, 0, 0), width=5)
        self.plotWidget = pg.PlotWidget(background='white')
        self.plotWidget = pg.PlotCurveItem(background='white')
        self.plotWidget.plot([1, 2, 3], [33, 35, 22], pen=pen, fillLevel=True)
        self.plotWidget.setYRange(min=1, max=100)
        self.plotWidget.setTitle('Memory Usage Percentage')
        self.plotWidget.showGrid(x=True, y=True)

        self.widget.setLayout(self.mainLayout)
        self.mainLayout.addWidget(self.appTitle)
        self.mainLayout.addLayout(self.firstLineLayout)
        self.mainLayout.addWidget(self.plotWidget)
        print(psutil.virtual_memory())
        print(34359738368 / 32768)
        print()
        

if __name__ == "__main__":
    app = QApplication([])
    memUs = MemoryUsage()
    memUs.show()
    sys.exit(app.exec())
    