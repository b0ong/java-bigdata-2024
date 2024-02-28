# file: p38_qtApp.py
# desc: pyqt5, QtDesigner를 같이 사용 

'''
설치 > pip install PyQt5
설치> pip install PyQt5Designer
'''
import sys
from PyQt5 import QtGui, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 

class qtApp(QWidget): 
    def __init__(self) -> None: 
        super().__init__() 
        self.initUI()        
        
    def initUI(self): # ui파일을 로드에서 화면디자인 사용
        uic.loadUi('./day06/firstApp.ui', self)            
        self.setWindowIcon(QIcon('./images/apple-logo.png'))
        #버튼 시그널처리
        self.btnMsg.clicked.connect(self.btnMsgCliked) # ui파일내 위젯은 자동완성x 
        
        self.show()
        
    def btnMsgCliked(self):
        self.label.setText('What the F**!')
        QMessageBox.about(self, 'Qt디자이너','클릭하였습니다!')
        
    def btn1Clicked(self):
        QMessageBox.about(self, '버튼클릭','버튼을 눌렀습니다!')    
        
    def closeEvent(self, QcloseEvent) -> None: 
        re = QMessageBox.question(self, '종료확인','종료하겠습니까?', QMessageBox.Yes|QMessageBox.Cancel)
        if re == QMessageBox.Yes: 
            QcloseEvent.accept()
        else:
            QcloseEvent.ignore() 
        
                       
app = QApplication(sys.argv) 
app.setWindowIcon(QIcon('./images/apple-logo.png'))     
inst = qtApp() 
app.exec_() 