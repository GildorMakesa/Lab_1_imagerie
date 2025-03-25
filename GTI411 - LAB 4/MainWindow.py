from PyQt5 import QtWidgets
from Lab4.controller import Lab4Controller



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controller = Lab4Controller()
    sys.exit(app.exec_())
