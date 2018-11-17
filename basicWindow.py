import sys
from PyQt5 import QtWidgets, QtGui

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    l1 = QtWidgets.QLabel(w)
    l2 = QtWidgets.QLabel(w)
    l1.setText('hello world')
    l2.setPixmap(QtGui.QPixmap('globe.png'))
    w.setWindowTitle('PyQt5 lesson 1')
    w.setGeometry(100,100,300,200) #(position of the window, size of the window)
    l1.move(130,20) #label postion
    l2.move(120,90)
    w.show()
    sys.exit(app.exec_())
window()