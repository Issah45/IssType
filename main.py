from PyQt6.QtWidgets import *
from PyQt6 import uic
from PyQt6.QtGui import QFont
from PyQt6.QtGui import QShortcut, QKeySequence

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("editor.ui", self)
        
        self.show()
        
        self.actionSetFont.triggered.connect(self.set_font)

        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)
        self.openButton.clicked.connect(self.open_file_combo)

        openS = QShortcut(QKeySequence("Ctrl+O"), self)
        saveS = QShortcut(QKeySequence("Ctrl+S"), self)

        openS.activated.connect(self.open_file)
        saveS.activated.connect(self.save_file)
    
    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")
        if filename != "":
            with open(filename, "r") as f:
                self.plainTextEdit.setPlainText(f.read())
        self.comboBox.addItem(filename)
    
    def open_file_combo(self):
        filename = self.comboBox.currentText()
        if filename != "":
            with open(filename, "r") as f:
                self.plainTextEdit.setPlainText(f.read())
    
    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)")
        if filename != "":
            with open(filename, "w") as f:
                f.write(self.plainTextEdit.toPlainText())
        self.comboBox.addItem(filename)
    
    def set_font(self):
        font, valid = QFontDialog.getFont()
        if valid:
            self.plainTextEdit.setFont(font)

app = QApplication([])
window = MyGUI()
app.exec()