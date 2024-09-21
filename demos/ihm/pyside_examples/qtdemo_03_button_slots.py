import sys
import random
from PySide6 import QtCore, QtWidgets

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self._hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self._label = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)
        self._button = QtWidgets.QPushButton('Click Me')

        self._layout = QtWidgets.QVBoxLayout(self)
        self._layout.addWidget(self._label)
        self._layout.addWidget(self._button)

        self._button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self._label.setText(random.choice(self._hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    #widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())