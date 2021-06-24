import sys  #command line argument
import time
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *



app = QApplication(sys.argv)
due = input("Enter Time for Alert (format: hh:mm): ")
message = input("Enter your Message for Alert: ")

try:
    hourse, mins = due.split(":")
    due = QTime(int(hourse), int(mins))
    if not due.isValid():
        raise ValueError
except ValueError:
    message = "Time entered is not a valid time"
while QTime.currentTime() < due:
    time.sleep(20)

label = QLabel("<font color=blue size=77><br>" +message+ "</br></font>")
label.setWindowFlags(Qt.SplashScreen)
label.show()
QTimer.singleShot(60000, app.quit)
sys.exit(app.exec_())



