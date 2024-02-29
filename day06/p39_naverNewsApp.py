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
            # html 태그, 특수문자 삭제를 해야함(<b>손흥민</b>, &lt;[<], &gt;[>], &quot;["], &nbsp;[ ]) 
            title = str(post['title']).replace('<b>', '').replace('</b>', '').replace('&quot;', '"')
            
            
            self.tblSearchResult.setItem(n, 0, QTableWidgetItem(title))
            self.tblSearchResult.setItem(n, 1, QTableWidgetItem(post['link']))
            # 현재날짜 thu, 29 Feb 2024 09:00:00 +09:00 를 2024-02-29로 변경하는 작업
            tempDates = str(post['pubDate']).split(' ') 
            year = tempDates[3]
            month = time.strptime(self.changeMonthFormat(tempDates[2]), "%m").tm_mon # Feb, Mar 같은 영어단축이름을 2,3 월에 대한 숫자로 변경하는 로직
            month = f'{month:02d}' # 월에 대한 두자리 만들때 01, 02
            day = tempDates[1]
            date = f'{year}-{month}-{day}'
            # # 여기까지
            self.tblSearchResult.setItem(n, 2, QTableWidgetItem(date))
            n += 1
            
            self.tblSearchResult.setColumnWidth(0, 430) #QTable에 가로 스크롤 없애기 위해서 넓이 조절
            self.tblSearchResult.setColumnWidth(1, 200)
            self.tblSearchResult.setEditTriggers(QAbstractItemView.NoEditTriggers)
    
    def changeMonthFormat(self, month):
        if month == "Jan":
            return "1"
        elif month == "Feb":
            return "2"
        elif month == "Mar":
            return "3"
        elif month == "Apr":
            return "4"
        elif month == "May":
            return "5"
        elif month == "Jun":
            return "6"
        elif month == "Jul":
            return "7"
        elif month == "Aug":
            return "8"
        elif month == "Sep":
            return "9"
        elif month == "Oct":
            return "10"
        elif month == "Nov":
            return "11"
        elif month == "Dec":
            return "12"    

            
        
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