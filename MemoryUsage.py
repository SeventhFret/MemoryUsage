from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QLabel, QPushButton, QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget
from PySide6.QtGui import Qt, QFont, QPixmap, QIcon
import pyqtgraph as pg
import sys
import psutil

class MemoryUsage(QMainWindow):
    def __init__(self):
        # ^ Initializing parent class
        super().__init__()

        # ^ Setting attribute mem_data which includes svmem object
        self.mem_data = psutil.virtual_memory()

        # ^ Setting plot data
        self.x = [0]
        self.y = [self.mem_data.percent]
        

        # ^ Initialize user interface
        self.initUI()

        # ^ Setting up the plot data
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_graph)
        self.timer.timeout.connect(self.update_values)
        self.timer.setInterval(1000)
        self.timer.start()

    def initUI(self):
        self.setFixedSize(600, 600)
        self.setUpdatesEnabled(True)
        self.setWindowTitle('Memory Usage')
        self.setStyleSheet('''background-color: black;''')

        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)

        # ^ FONTS
        self.font40 = QFont("Georgia", 40, 700)
        self.font25 = QFont("Georgia", 25, 700)
        self.fontDigits = QFont("Hack", 25, 700)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.setAlignment(Qt.AlignCenter)


        # ^ MAIN LABEL
        self.appTitle = QLabel(text='Memory Usage Program')
        self.appTitle.setFont(self.font40)
        self.appTitle.setAlignment(Qt.AlignCenter)
        

        # ^ FIRST LINE LABELS
        self.firstLineText = QLabel('Total Memory:')
        self.firstLineText.setFont(self.font25)
        self.firstLineText.setStyleSheet('''color: maroon;
margin-top: 20%;''')
        self.firstLineText.setAlignment(Qt.AlignCenter)

        self.firstLineText2 = QLabel(f'{self.mem_data.total // 1024 ** 3} Gb')
        self.firstLineText2.setFont(self.fontDigits)
        self.firstLineText2.setStyleSheet('margin-top: 20%;')
        self.firstLineText2.setAlignment(Qt.AlignCenter)

        self.firstLineLayout = QHBoxLayout()
        self.firstLineLayout.setAlignment(Qt.AlignCenter)
        self.firstLineLayout.addWidget(self.firstLineText)
        self.firstLineLayout.addWidget(self.firstLineText2)



        # ^ SECOND LINE LABELS
        self.secondLineText = QLabel('Used memory:')
        self.secondLineText.setFont(self.font25)
        self.secondLineText.setStyleSheet('''color: maroon;
margin-top: 20%;''')
        self.secondLineText.setAlignment(Qt.AlignCenter)                                          

        self.secondLineText2 = QLabel(f'{(self.mem_data.used / 1024 ** 3):.3f} Gb')
        self.secondLineText2.setFont(self.fontDigits)
        self.secondLineText2.setStyleSheet('margin-top: 20%;')
        self.secondLineText2.setAlignment(Qt.AlignCenter)                                          

        self.secondLineButton = QPushButton('')
        self.secondLineButton.setIcon(QPixmap('./info.png'))
        self.secondLineButton.setToolTip('''The used value is not necessarily equal to the difference
between total and available, because some memory
may be occupied by processes that have not yet
freed it.''')
        self.secondLineButton.setStyleSheet('margin-top: 10%;')
        # self.secondLineButton.setIconSize(self.secondLineButton.size())


        self.secondLineLayout = QHBoxLayout()
        self.secondLineLayout.setAlignment(Qt.AlignCenter)
        self.secondLineLayout.addWidget(self.secondLineText)
        self.secondLineLayout.addWidget(self.secondLineText2)
        self.secondLineLayout.addWidget(self.secondLineButton)



        # ^ THIRD LINE LABELS
        self.thirdLineText = QLabel('Available memory:')
        self.thirdLineText.setFont(self.font25)
        self.thirdLineText.setStyleSheet('''color: maroon;
margin-top: 20%;''')
        self.thirdLineText.setAlignment(Qt.AlignCenter)                                          

        self.thirdLineText2 = QLabel(f'{(self.mem_data.available / 1024 ** 3):.3f} Gb')
        self.thirdLineText2.setFont(self.fontDigits)
        self.thirdLineText2.setStyleSheet('margin-top: 20%;')
        self.thirdLineText2.setAlignment(Qt.AlignCenter)                                          

        

        self.thirdLineLayout = QHBoxLayout()
        self.thirdLineLayout.setAlignment(Qt.AlignCenter)
        self.thirdLineLayout.addWidget(self.thirdLineText)
        self.thirdLineLayout.addWidget(self.thirdLineText2)



        # ^ FOURTH LINE LABELS
        self.fourthLineText = QLabel('Percentage:')
        self.fourthLineText.setFont(self.font25)
        self.fourthLineText.setStyleSheet('''color: maroon;
margin-top: 20%;''')
        self.fourthLineText.setAlignment(Qt.AlignCenter)                                          

        self.fourthLineText2 = QLabel(f'{self.mem_data.percent}%')
        self.fourthLineText2.setFont(self.fontDigits)
        self.fourthLineText2.setStyleSheet('margin-top: 20%;')
        self.fourthLineText2.setAlignment(Qt.AlignCenter)     

        self.fourthLineLayout = QHBoxLayout()
        self.fourthLineLayout.setAlignment(Qt.AlignCenter)
        self.fourthLineLayout.addWidget(self.fourthLineText)
        self.fourthLineLayout.addWidget(self.fourthLineText2)


        # ^ PLOTTING
        pen = pg.mkPen(color=(128, 0, 0), width=5)
        self.plotWidget = pg.PlotWidget(background=None)
        self.plotWidget.setMouseEnabled(x=False, y=False)
        x_axis = self.plotWidget.getAxis('bottom')  # отримуємо об'єкт AxisItem для осі x
        x_axis.setLabel('Time', units='s')  # встановлюємо підпис та одиниці виміру для осі x

        y_axis = self.plotWidget.getAxis('left')  # отримуємо об'єкт AxisItem для осі y
        y_axis.setLabel('Percent', units='%')  # встановлюємо підпис та одиниці виміру для осі y



        self.data_line = self.plotWidget.plot(self.x, self.y, pen=pen, fillLevel=True)
        self.plotWidget.setYRange(min=1, max=100)
        self.plotWidget.setTitle('Memory Usage Percentage')
        self.plotWidget.showGrid(x=True, y=True)


        # ^ Setting all layouts
        self.widget.setLayout(self.mainLayout)
        self.mainLayout.addWidget(self.appTitle)
        self.mainLayout.addLayout(self.firstLineLayout)
        self.mainLayout.addLayout(self.secondLineLayout)
        self.mainLayout.addLayout(self.thirdLineLayout)
        self.mainLayout.addLayout(self.fourthLineLayout)
        self.mainLayout.addWidget(self.plotWidget)

        

    def update_graph(self):
        self.mem_data = psutil.virtual_memory()
        self.plotWidget.setYRange(min=int(((self.mem_data.percent // 10) - 2) * 10), max=int(((self.mem_data.percent // 10) + 2) * 10))
        if len(self.x) > 7 and len(self.y) > 7:
            self.x = self.x[1:]
            self.x.append(self.x[-1] + 1)
            self.y = self.y[1:]
            self.y.append(self.mem_data.percent)
        else:
            self.x.append(self.x[-1] + 1)
            self.y.append(self.mem_data.percent)
        self.data_line.setData(self.x, self.y)


    def update_values(self):
        self.mem_data = psutil.virtual_memory()
        self.secondLineText2.setText(f'{(self.mem_data.used / 1024 ** 3):.3f} Gb')
        self.thirdLineText2.setText(f'{(self.mem_data.available / 1024 ** 3):.3f} Gb')
        self.fourthLineText2.setText(f'{self.mem_data.percent}%')

        

if __name__ == "__main__":
    app = QApplication([])
    memUs = MemoryUsage()
    memUs.show()
    sys.exit(app.exec())
    