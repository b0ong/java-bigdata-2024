# file: p47_qrCodeApp.py
# desc: pyQt5 QR코드 앱
# pip3 install qrcode

import sys
from PyQt5 import QtGui, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 
import qrcode

class qtApp(QWidget): 
    def __init__(self) -> None: 
        super().__init__() 
        self.initUI()        
        
    def initUI(self): # ui파일을 로드에서 화면디자인 사용
        uic.loadUi('./day07/qrApp.ui', self)      
        self.setWindowTitle('QR코드 생성기')      
        self.setWindowIcon(QIcon('./images/apple-logo.png'))
        #버튼 시그널처리
        self.btnTrans.clicked.connect(self.btnTransCliked) # ui파일내 위젯은 자동완성x 
        
        self.show()
        
    def btnTransCliked(self):
        data = self.txtQrData.text()
        
        if len(data.strip()) == 0:
            QMessageBox.about(self,'경고', '데이터 입력')
            return
        else:
            imgpath = './day07/qr.png'
            qrImage = qrcode.make(data)
            qrImage.save(imgpath)
            img = QPixmap(imgpath)
            self.lblQrCode.setPixmap(QPixmap(img).scaledToWidth(300))
            
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