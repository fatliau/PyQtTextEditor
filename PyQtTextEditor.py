#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 02:57:54 2018

@author: JC
"""
import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQt tuts!")
        self.setWindowIcon(QtGui.QIcon('mrbean.png'))
        
        extractAction = QtGui.QAction("&GET TO THE COPPAH!!", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("Leave the App")
        extractAction.triggered.connect(self.close_application)
        
        openEditor = QtGui.QAction("&Editor", self)
        openEditor.setShortcut("Ctrl+E")
        openEditor.setStatusTip('Open Editor')
        openEditor.triggered.connect(self.editor)
        
        openFile = QtGui.QAction("&Open File", self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)
        
        saveFile = QtGui.QAction("&Save Dile", self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.file_save)
        
        self.statusBar()
        
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(extractAction)
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
        
        editorMenu = mainMenu.addMenu("&Editor")
        editorMenu.addAction(openEditor)
        
        self.home()
        
    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(100,100)
        
        extractAction = QtGui.QAction(QtGui.QIcon('mrbean.png'), "Flee the scene", self)
        extractAction.triggered.connect(self.close_application)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)
        
        fontChoice = QtGui.QAction('Font', self)
        fontChoice.triggered.connect(self.font_choice)
        self.toolBar = self.addToolBar("Font")
        self.toolBar.addAction(fontChoice)
        
        color = QtGui.QColor(0, 0, 0)
        fontColor = QtGui.QAction('Font bg color', self)
        fontColor.triggered.connect(self.color_picker)
        self.toolBar.addAction(fontColor)
        
        checkBox = QtGui.QCheckBox("Enlarge Window", self)
        checkBox.move(100,25)
        checkBox.toggle()
        checkBox.stateChanged.connect(self.enlarge_window)
        
        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)
        
        self.btn = QtGui.QPushButton("Download", self)
        self.btn.move(200, 120)
        self.btn.clicked.connect(self.download)
        
        print(self.style().objectName())
        self.styleChoice = QtGui.QLabel("Windows", self)
        
        comboBox = QtGui.QComboBox(self)
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        comboBox.addItem("windowsvista")
        
        comboBox.move(50,250)
        self.styleChoice.move(50,150)
        comboBox.activated[str].connect(self.style_choice)
    
        cal = QtGui.QCalendarWidget(self)
        cal.move(500, 200)
        cal.resize(200, 200)
        
        self.show()

        
    def file_open(self):
        name = QtGui.QFileDialog.getOpenFileName(self, "Open File")
        file = open(name, 'r')
        self.editor()
        
        with file:
            text = file.read()
            self.textEdit.setText(text)
            
    def file_save(self):
        name = QtGui.QFileDialog.getSaveFileName(self, "Save File")
        file = open(name, 'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()
        
        
    def editor(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        
    def color_picker(self):
        color = QtGui.QColorDialog.getColor()
        self.styleChoice.setStyleSheet("QWidget { background-color: %s}" % color.name())
        
    def font_choice(self):
        font, valid = QtGui.QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)
        
    def style_choice(self,text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QstyleFactory.create(text))
        
    def download(self):
        self.completed = 0
        while self.completed < 100:
            self.completed += 0.00005
            self.progress.setValue(self.completed)
    
    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50, 50, 1000, 1000)
        else:
            self.setGeometry(50, 50, 500, 300)
    
    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Extract!', "Get into the chopper?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("whooaaa so custom!!!")
            sys.exit()
        else:
            self.setWindowTitle("PyQt tuts!!!!!!!")
            pass
        
        
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
    
run()

