import sys
import os
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.configure()
        

    def configure(self):
        self.workdir = ""
        self.ui.btn_dir.clicked.connect(self.open_dir)
    
    def open_dir(self):
        self.workdir = QFileDialog.getExistingDirectory(self, "Виберіть папку", os.getcwd())
        if self.workdir:
            self.ui.lw_files.clear()
            for file in os.listdir(self.workdir):
                if file.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                    self.ui.lw_files.addItem(file)   
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())
