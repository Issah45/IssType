from PyQt6.QtWidgets import *
from PyQt6 import uic
from PyQt6.QtGui import QFont
from PyQt6.QtGui import QShortcut, QKeySequence

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("editor.ui", self)
        self.show()
        self.action12pt.triggered.connect(lambda: self.change_size(12))
        self.action18pt.triggered.connect(lambda: self.change_size(18))
        self.action24pt.triggered.connect(lambda: self.change_size(24))
        self.action32pt.triggered.connect(lambda: self.change_size(32))

        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)

        openS = QShortcut(QKeySequence("Ctrl+O"), self)
        saveS = QShortcut(QKeySequence("Ctrl+S"), self)

        openS.activated.connect(self.open_file)
        saveS.activated.connect(self.save_file)
    
    def change_size(self, size):
        self.plainTextEdit.setFont(QFont("Arial", size))
    
    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")
        if filename != "":
            with open(filename, "r") as f:
                self.plainTextEdit.setPlainText(f.read())
    
    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)")
        if filename != "":
            with open(filename, "w") as f:
                f.write(self.plainTextEdit.toPlainText())

app = QApplication([])
window = MyGUI()
app.exec()