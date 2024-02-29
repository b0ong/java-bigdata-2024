# file: p39_naverNewsApp.py
# desc: pyqt5, QtDesigner naver API 연동 

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

import webbrowser #
from naverSearch import NaverSearch 
import datetime
import time

class qtApp(QWidget): 
    def __init__(self) -> None: 
        super().__init__() 
        self.initUI()        
        
    def initUI(self): # ui파일을 로드에서 화면디자인 사용
        uic.loadUi('./day06/naverNews.ui', self)       # ui 파일 맞춰서 변경     
        self.setWindowIcon(QIcon('./images/news.png')) 
        #버튼 시그널처리
        self.btnSearch.clicked.connect(self.btnSearchCliked) # ui파일내 위젯은 자동완성x 
        self.txtSearchWord.returnPressed.connect(self.btnSearchCliked) # 검색버튼 시그널 함수를 연결
        self.tblSearchResult.itemSelectionChanged.connect(self.tblResultSelected) 
        
        self.show()

    def tblResultSelected(self): # 테이블 클리시 처리
        selectRow = self.tblSearchResult.currentRow() # 현재 선택된 행의 인덱스
        url = self.tblSearchResult.item(selectRow, 1).text()
        #QMessageBox.about(self, 'popup', url) 
        webbrowser.open(url)
                
    def btnSearchCliked(self): # 검색버튼 클릭시 처리
        searchWord = self.txtSearchWord.text().strip()
        if (len(searchWord)) == 0:
            QMessageBox.about(self, '네이버검색','검색색어를 입력해주세요!')
            return # 함수 탈출
                
        #QMessageBox.about(self, '네이버검색','검색시작!')
        #검색시작
        api = NaverSearch() # api 객체 생성
        jsonSearch = api.getSearchResult(searchWord)
        #print(jsonSearch)
        self.makeTable(jsonSearch) # 검색결과로 리스트뷰를 만드는 함수 호출
    
    def makeTable(self, data):
        result = data['items'] # 네이버 검색결과의 키 items의 값들만 활용
        # tblSearchResult 리스트뷰 작업시작
        self.tblSearchResult.setColumnCount(3)
        self.tblSearchResult.setRowCount(len(result)) # 10개면 10개
        self.tblSearchResult.setHorizontalHeaderLabels(['기사제목','뉴스링크','게시일자'])
        
        n = 0
        for post in result:
            self.tblSearchResult.setItem(n, 0, QTableWidgetItem(post['title']))
            self.tblSearchResult.setItem(n, 1, QTableWidgetItem(post['link']))
            # tempDates = str(post['pubDate']).split(' ') # 내일설명
            # year = tempDates[3]
            # month = time.strptime(tempDates[2], '%d').tm_mon
            # day = tempDates[1]
            # date = f'{year}-{month}-{day}'
            # self.tblSearchResult.setItem(n, 2, QTableWidgetItem(date))
            # self.tblSearchResult.setItem(n, 2, QTableWidgetItem('나중에'))
            n += 1
            
            self.tblSearchResult.setColumnWidth(0, 465)
            self.tblSearchResult.setColumnWidth(1, 200)
            self.tblSearchResult.setEditTriggers(QAbstractItemView.NoEditTriggers)
            
        
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