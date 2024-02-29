# file: p47_transApp.py
# desc: pyQt5 구글번역앱
# pip3 install googletrans
# 모듈 라이브러리 설치시 버전 업/다운, 버전을 기재해주면 됨!
#> pip3 install googletrans==3.1.0a0
#> pip3 install googletrans==4.0.0rc1

import sys
from PyQt5 import QtGui, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 

from googletrans import Translator

class qtApp(QWidget): 
    def __init__(self) -> None: 
        super().__init__() 
        self.initUI()     
        self.myTrans = Translator() # 구글번역기 객체생성   
        
    def initUI(self): # ui파일을 로드에서 화면디자인 사용
        uic.loadUi('./day07/transApp.ui', self)      
        self.setWindowTitle('구글번역앱')      
        self.setWindowIcon(QIcon('./images/apple-logo.png'))
        #버튼 시그널처리
        self.btnTrans.clicked.connect(self.btnTransCliked) # ui파일내 위젯은 자동완성x 
        self.txtBaseText.returnPressed.connect(self.btnTransCliked) 
        self.show()
        
    def btnTransCliked(self):
        #QMessageBox.about(self,'번역','번역시작!')            
        text = self.txtBaseText.text().strip()
        if len(text) != 0:
            result = self.myTrans.translate(text, src='auto', dest='en')
            self.txbResult.append(result.text)
            
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