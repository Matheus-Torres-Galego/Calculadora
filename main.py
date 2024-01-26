import sys
from PySide6.QtGui import QIcon
from display import Display
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH
from main_window import MainWindow, Info
from styles import Theme
from buttons import ButtonsGrid

if __name__ == "__main__":
    # Cria a Aplicação
    app = QApplication(sys.argv)
    Theme(app)
    window = MainWindow()

    # Definir o Icone do App
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # info
    info = Info("2.0 ^ 10.0 = 1024.0")
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    display.setPlaceholderText("Digite Algo.")
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display)
    window.vLayout.addLayout(buttonsGrid)


    # Executa Tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
