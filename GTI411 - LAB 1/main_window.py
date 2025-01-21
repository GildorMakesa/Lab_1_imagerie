from PyQt5 import QtWidgets
from Lab1.controllers.lab1_controller import Lab1Controller



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controller = Lab1Controller()
    sys.exit(app.exec_())
