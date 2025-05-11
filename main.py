import sys
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui import Ui_MainWindow
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageFilter

class ImageProcessor():
    def __init__(self, label_widget):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/"
        self.label = label_widget

    def loadImage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)

    def do_bw(self):
        if self.image:
            self.image = self.image.convert("L")
            self.saveImage()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
    
    def do_flip(self):
        if self.image:
            self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
            self.saveImage()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
    
    def do_rotate(self, angle):
        if self.image:
            self.image = self.image.transpose(Image.ROTATE_90 if angle > 0 else Image.ROTATE_270)
            self.saveImage()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
    
    def do_sharp(self):
        if self.image:
            self.image = self.image.filter(ImageFilter.SHARPEN)
            self.saveImage()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)

    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)
        os.makedirs(path, exist_ok=True)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

    def showImage(self, path):
        self.label.hide()
        pixmapimage = QPixmap(path)
        w, h = self.label.width(), self.label.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        self.label.setPixmap(pixmapimage)
        self.label.show()

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.configure()
        
    def configure(self):
        self.workdir = ""
        self.workimage = ImageProcessor(self.ui.lb_image)
        
        self.ui.btn_dir.clicked.connect(self.open_dir)
        self.ui.lw_files.currentRowChanged.connect(self.show_chosen_image)
        self.ui.btn_bw.clicked.connect(self.workimage.do_bw)
        self.ui.btn_flip.clicked.connect(self.workimage.do_flip)
        self.ui.btn_right.clicked.connect(lambda: self.workimage.do_rotate(-90))
        self.ui.btn_left.clicked.connect(lambda: self.workimage.do_rotate(90))
        self.ui.btn_sharp.clicked.connect(self.workimage.do_sharp)
        
    def open_dir(self):
        self.workdir = QFileDialog.getExistingDirectory(self, "Виберіть папку", os.getcwd())
        if self.workdir:
            self.ui.lw_files.clear()
            for file in os.listdir(self.workdir):
                print(file)
                if file.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                    self.ui.lw_files.addItem(file)

    def show_chosen_image(self):
        if self.ui.lw_files.currentRow() >= 0:
            filename = self.ui.lw_files.currentItem().text()
            self.workimage.loadImage(self.workdir, filename)
            image_path = os.path.join(self.workdir, filename)
            self.workimage.showImage(image_path)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())
