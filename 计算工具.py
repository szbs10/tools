import re
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from functools import *

class jisuangongju():

	def __init__(self):
		# 从文件中加载UI定义

		# 从 UI 定义中动态 创建一个相应的窗口对象
		self.ui = QUiLoader().load('计算工具.ui')

		self.ui.button0.clicked.connect(partial(self.jisuan,'0'))
		self.ui.button1.clicked.connect(partial(self.jisuan,'1'))
		self.ui.button2.clicked.connect(partial(self.jisuan,'2'))
		self.ui.button3.clicked.connect(partial(self.jisuan,'3'))
		self.ui.button4.clicked.connect(partial(self.jisuan,'4'))
		self.ui.button5.clicked.connect(partial(self.jisuan,'5'))
		self.ui.button6.clicked.connect(partial(self.jisuan,'6'))
		self.ui.button7.clicked.connect(partial(self.jisuan,'7'))
		self.ui.button8.clicked.connect(partial(self.jisuan,'8'))
		self.ui.button9.clicked.connect(partial(self.jisuan,'9'))
		self.ui.buttonjia.clicked.connect(partial(self.jisuan,'+'))
		self.ui.buttonjian.clicked.connect(partial(self.jisuan,'-'))
		self.ui.buttoncheng.clicked.connect(partial(self.jisuan,'*'))
		self.ui.buttonchu.clicked.connect(partial(self.jisuan,'/'))
		self.ui.buttonzuokuohao.clicked.connect(partial(self.jisuan,'('))
		self.ui.buttonyoukuohao.clicked.connect(partial(self.jisuan,')'))
		self.ui.buttondian.clicked.connect(partial(self.jisuan,'.'))
		self.ui.buttonchengfang.clicked.connect(partial(self.jisuan,'**'))
		self.ui.buttonshanchu.clicked.connect(self.shanchu)
		self.ui.buttondengyu.clicked.connect(self.dengyu)


	def jisuan(self,thing):
		text = self.ui.shizi.text()
		self.ui.shizi.setText(text + thing)

	def shanchu(self):
		text = self.ui.shizi.text()
		self.ui.shizi.setText(text[:len(text)-1])

	def dengyu(self):
		text = self.ui.shizi.text()
		try:
			text = eval(text)
			self.ui.shizi.setText(str(text))
		except:
			QMessageBox.about(self.ui,'警告','输入不合规')



app = QApplication(sys.argv)
jisuangongju = jisuangongju()
jisuangongju.ui.show()
sys.exit(app.exec_())