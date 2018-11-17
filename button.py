import sys
from PyQt5 import QtWidgets, QtGui

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    b = QtWidgets.QPushButton(w)
    l = QtWidgets.QLabel(w)
    b.setText('Push me')
    l.setText('Look at me')
    w.setWindowTitle('PyQt5 lesson 1')
    w.setGeometry(100,100,300,200) #(position of the window, size of the window)
    b.move(100,50)
    l.move(110,100)
    w.show()
    sys.exit(app.exec_())
window()