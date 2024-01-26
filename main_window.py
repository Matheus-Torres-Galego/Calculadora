from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QMainWindow, QVBoxLayout, QWidget, QLabel
from variables import SMALL_FONT_SIZE


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Layout do App
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        # Titulo do App
        self.setWindowTitle("Calculadora")

        # Add um Widget

    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)

        # Ultima Coisa a Ser Feito

    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())


# Criando o texto
class Info(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    # Definindo as Config
    def configStyle(self):
        self.setStyleSheet(f"font-size: {SMALL_FONT_SIZE}px;")
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
