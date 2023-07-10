import os
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, 
    QLabel, QLineEdit, QGridLayout, QCheckBox, 
    QMessageBox, QFileDialog
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon
from pdf2image import convert_from_path

#inherit from QWidget
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("icon.png"))
        self.setWindowTitle("SplitPDF App")
        self.setContentsMargins(20,20,20,20)
        self.resize(550,320)
        
        #add label & text input boxes
        layout = QGridLayout()
        self.setLayout(layout)
        
        #open file button
        self.openFileButton = QPushButton("Open File",self)
        self.openFileButton.clicked.connect(self.show_file_picker)
        layout.addWidget(self.openFileButton,1,2)
        
        #input label
        self.inputLabel = QLabel("Pdf file path:")
        layout.addWidget(self.inputLabel,1,0)
        
        #input path
        self.inputPath = QLineEdit()
        self.inputPath.setMinimumSize(QSize(50,50))
        layout.addWidget(self.inputPath,1,1,1,1)
        
        #output label
        self.outputLabel = QLabel("Output path:")
        layout.addWidget(self.outputLabel,2,0)
        
        #output path
        self.outputPath = QLineEdit()
        self.outputPath.setMinimumSize(QSize(50,50))
        layout.addWidget(self.outputPath,2,1,1,2)
        
        #check to save in parent directory (autofill output directory)
        self.checkbox = QCheckBox("Save to parent directory")
        self.checkbox.stateChanged.connect(self.update_output)
        layout.addWidget(self.checkbox,3,0)
        
        #clear QLineEdit
        clearButton = QPushButton("Clear all inputs")
        clearButton.setFixedWidth(120)
        clearButton.clicked.connect(self.clear_all)
        layout.addWidget(clearButton,3,1,Qt.AlignmentFlag.AlignCenter)
        
        #run app button
        button = QPushButton("Run app")
        button.setFixedWidth(100)
        button.clicked.connect(self.splitpdf)
        layout.addWidget(button,3,2,Qt.AlignmentFlag.AlignCenter)
    
    #save to parent directory
    def update_output(self,state):
        if state == 2:
            new_text = os.path.split(self.inputPath.text())[0]
            self.outputPath.setText(new_text)
        else:
            pass

    #clear all
    def clear_all(self):
        self.checkbox.setChecked(False)
        self.inputPath.setText("")
        self.outputPath.setText("")
    
    #split pdf        
    def splitpdf(self):
        images = convert_from_path(self.inputPath.text())

        #add / if missing
        if self.outputPath.text()[-1] != "/":
            output_path = f"{self.outputPath.text()}/"
        else:
            output_path = self.outputPath.text()
    
        #create path if doesn't exist
        if not os.path.exists(output_path):
            os.makedirs(output_path)
    
        #save each page in jpg format
        for i in range(len(images)):
            images[i].save(f"{output_path}"+"page"+str(i)+".jpg","JPEG")
        
        #show message
        message = QMessageBox()
        message.setWindowTitle("App Run")
        message.setText("The input pdf file has been converted to series of jpg images.")
        message.setIcon(QMessageBox.Icon.Information)
        message.exec()

    #select file & send file_name (full path) to inputPath
    def show_file_picker(self):
        file_name, _ = QFileDialog.getOpenFileName(self,"Select pdf file","",
                                                   "Pdf Files (*.pdf);;All Files (*)")
        self.inputPath.setText(file_name)
        # return file_name

if __name__ == "__main__":
    #show window
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    #add css
    with open("./DesktopApp/styles.css","r") as file:
        app.setStyleSheet(file.read())

    #ensure app can quit properly
    sys.exit(app.exec())
