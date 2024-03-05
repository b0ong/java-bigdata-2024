# file: p66_unageEditor.py
# desc: PyQt 이미지 에디터
'''
qrc 파일을 사용하려면
> pyrcc5 "resources.qrc" -o "resources_rc.py"
'''

import sys
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QCloseEvent, QMouseEvent
from PyQt5.QtWidgets import *
#리소스 파일 추가
import resources_rc
# OpenCV 추가
import cv2

class WinApp(QMainWindow): #QWidget이 아님!!
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initSignal()

    def initUI(self):
        uic.loadUi('/Users/gukjinhan/Documents/GitHub/java-bigdata-2024/day09/pyNewPaint.ui',self)
        self.setWindowIcon(QIcon('/Users/gukjinhan/Documents/GitHub/java-bigdata-2024/day09/imgs/editor.png'))
        self.setWindowTitle('이미지에디터 v0.5')
        ## 이미지 추가/ 여러가지 UI에 대한 초기화
        pixmap = QPixmap('/Users/gukjinhan/Documents/GitHub/java-bigdata-2024/day09/tropical_beach.jpeg').scaledToHeight(471)
        self.lblCanvas.setPixmap(pixmap)
        self.brushColor = Qt.Red # 빨간색이 기본
        ## UI초기화 끝
        self.show()
        
    def initSignal(self):
        #메뉴/툴바 액션에 대한 시그널처리함수 선언..
        self.action_New.triggered.connect(self.actionNewClicked)
        self.action_New.triggered.connect(self.actionOpenClicked)
        self.action_New.triggered.connect(self.actionSaveClicked)
        self.action_New.triggered.connect(self.actionExitClicked)
        self.action_New.triggered.connect(self.actionPenRedClicked)
        self.action_New.triggered.connect(self.actionPenGreenClicked)
        self.action_New.triggered.connect(self.actionPenBuleClicked)
        self.action_New.triggered.connect(self.actionAboutClicked)
        
        
    def actionNewClicked(self):
        canvas = QPixmap(self.lblCanvas.width(), self.lblCanvas.height()) 
        canvas.fill(QColor('white'))
        self.lblCanvas.setPixmap(canvas)
        
    def actionNewClicked(self):
        QMessageBox.about(self,'알림', '새그림')
        
    def actionOpenClicked(self):
        image = QFileDialog.getOpenFileName(self, '이미지 열기', '', 'Image file(*.jpeg;*.png;*.gif)')
        imagePath = image[0]
        pixmap = QPixmap(imagePath).scaledToHeight(471)
        self.lblCanvas.adjustSize()
        
    def actionSaveClicked(self):
        filePath,_ = QFileDialog.getSaveFileName(self, '이미지저장', '', 'Image file(*.jpeg;*.png;*.gif)')
        if filePath == '': return
        pixmap = self.lblCanvas.pixmap()
        pixmap.save(filePath)
        
    def actionExitClicked(self):
        exit(0) # 종료
                
    def actionPenRedClicked(self):
        self.brushColor = Qt.red
        
    def actionPenGreenClicked(self):
        self.brushColor = Qt.green
        
    def actionPenBuleClicked(self):
        self.brushColor = Qt.blue
        
    def actionAboutClicked(self):
        QMessageBox.about(self,'알림', '이미지 에디터 v0.5')
        
    def mouseMoveEvent(self, e) -> None:
        print(e.x(), e.y())
        brush = QPainter(self.lblCanvas.pixmap()) # lblCanvas에 브러쉬 하나 생성
        brush.setPen(QPen(self.brushColor, 3.5, style=Qt.SolidLine, cap= Qt.RoundCap))
        brush.drawPoint(e.x(), e.y())
        brush.end()
        self.update() # 화면 업데이트
    
    def closeEvent(self, a0: QCloseEvent) -> None:
        re = QMessageBox.question(self, '종료', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: QCloseEvent.accept()
        else: QCloseEvent.ignore()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ins = WinApp()
    sys.exit(app.exec_())