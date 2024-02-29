# file: p44_nothread.py
# desc: 


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
        uic.loadUi('./day07/testThread.ui', self)      
        self.setWindowTitle('노쓰레드앱')      
        self.setWindowIcon(QIcon('./images/apple-logo.png'))
        #버튼 시그널처리
        self.btnTrans.clicked.connect(self.btnTransCliked) # ui파일내 위젯은 자동완성x 
        
        self.show()
        
    def btnTransCliked(self):
        self.pgbTask.setValue(0) # 재설정
        self.pgbTask.setRange(0, 999_999) # 프로그레스 바 범위설정
        self.btnTrans.setDisabled(True)
        # UI(메인) 스레드가 화면을 그릴 수 있는 여유가 없음(응답앖음 발생)
        for i in range(0, 1_000_000): # 0~999,999
            print(f'노쓰레드 진행 >> {i}')
            self.pgbTask.setValue(i)
            self.txbLog.append(f'노쓰레드 진행 >> {i}')
       
        self.btnTrans.setEnabled(True)
        
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