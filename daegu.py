import requests
from bs4 import BeautifulSoup as bs
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
import webbrowser

a = []
x, y = 20, 20


page = requests.get("https://www.daegu.ac.kr/article/DG159/list")
soup = bs(page.content, "html.parser")

elements = soup.select('tr')
for element in elements:
    if element.text.strip()[0] == '2':
        aa = element.find('a')
        bb = aa["onclick"][9:15]
        a.append([aa.text.strip(),bb])


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global x, y
        self.setWindowTitle("대구대학교 공지사항")
        self.label = QLabel(a[0][0], self)
        self.label.move(x, y)
        btn1 = QPushButton("이동", self)
        btn1.move(320, y-4)
        btn1.clicked.connect(lambda : self.click(a[0][1]))
        y += 30
        
        self.label = QLabel(a[1][0], self)
        self.label.move(x, y)
        btn1 = QPushButton("이동", self)
        btn1.move(320, y-4)
        btn1.clicked.connect(lambda : self.click(a[1][1]))
        y += 30
        
        self.label = QLabel(a[2][0], self)
        self.label.move(x, y)
        btn1 = QPushButton("이동", self)
        btn1.move(320, y-4)
        btn1.clicked.connect(lambda : self.click(a[2][1]))
        y += 30
        
        self.label = QLabel(a[3][0], self)
        self.label.move(x, y)
        btn1 = QPushButton("이동", self)
        btn1.move(320, y-4)
        btn1.clicked.connect(lambda : self.click(a[3][1]))
        y += 30
        
        self.label = QLabel(a[4][0], self)
        self.label.move(x, y)
        btn1 = QPushButton("이동", self)
        btn1.move(320, y-4)
        btn1.clicked.connect(lambda : self.click(a[4][1]))
        y += 30
        
        self.label = QLabel(a[5][0], self)
        self.label.move(x, y)
        btn1 = QPushButton("이동", self)
        btn1.move(320, y-4)
        btn1.clicked.connect(lambda : self.click(a[5][1]))
        y += 30
        
        self.label = QLabel(a[6][0], self)
        self.label.move(x, y)
        btn1 = QPushButton("이동", self)
        btn1.move(320, y-4)
        btn1.clicked.connect(lambda : self.click(a[6][1]))
        y += 30

        self.setGeometry(300, 300, 420, 240)
        self.show()
    
    def click(self, link):
        webbrowser.open("https://www.daegu.ac.kr/article/DG159/detail/"+link)
        # print(link)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())