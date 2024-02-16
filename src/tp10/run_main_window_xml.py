"""
   
 auth : l.devigne

"""
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication


def main():
    app = QApplication([])
    ui_file_name = "main.ui"
    ui_file = QFile(ui_file_name)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()

    window.show()
    app.exec()


if __name__ == '__main__':
    main()
