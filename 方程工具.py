import re
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from functools import *
from sympy import *

class fangchenggongju():

	def __init__(self):
		# 从文件中加载UI定义

		# 从 UI 定义中动态 创建一个相应的窗口对象
		self.ui = QUiLoader().load('方程工具.ui')

		self.ui.button1.clicked.connect(self.yiyuanfangcheng)
		self.ui.button2.clicked.connect(self.duoyuanfangcheng)
		self.ui.button3.clicked.connect(self.kuozhangongju)

	def yiyuanfangcheng(self):
		text = self.ui.fangcheng1.text()
		x = symbols('x')
		try:
			result = solve(text)
			res = ''
			for i in range(len(result)):
				res += 'x'+str(i+1)+'='+str(result[i])+'\n'
			QMessageBox.about(self.ui,'结果',res)
		except:
			QMessageBox.about(self.ui,'警告','方程式不合规')

	def duoyuanfangcheng(self):		
		#QMessageBox.about(self.ui,'警告','此为付费功能')
		f = self.ui.fangcheng2.toPlainText()
		fc = f.splitlines()

		if len(fc) == 1:
			x1 = symbols('x1')
			wzs = [x1]
		if len(fc) == 2:
			x1,x2 = symbols('x1,x2')
			wzs = [x1,x2]
		if len(fc) == 3:
			x1,x2,x3 = symbols('x1,x2,x3')
			wzs = [x1,x2,x3]
		if len(fc) == 4:
			x1,x2,x3,x4 = symbols('x1,x2,x3,x4')
			wzs = [x1,x2,x3,x4]
		if len(fc) == 5:
			x1,x2,x3,x4,x5 = symbols('x1,x2,x3,x4,x5')
			wzs = [x1,x2,x3,x4,x5]	
		if len(fc) == 6:
			x1,x2,x3,x4,x5,x6 = symbols('x1,x2,x3,x4,x5,x6')
			wzs = [x1,x2,x3,x4,x5,x6]	
		if len(fc) == 7:
			x1,x2,x3,x4,x5,x6,x7 = symbols('x1,x2,x3,x4,x5,x6,x7')
			wzs = [x1,x2,x3,x4,x5,x6,x7]
		if len(fc) == 8:
			x1,x2,x3,x4,x5,x6,x7,x8 = symbols('x1,x2,x3,x4,x5,x6,x7,x8')
			wzs = [x1,x2,x3,x4,x5,x6,x7,x8]	
		if len(fc) == 9:
			x1,x2,x3,x4,x5,x6,x7,x8,x9 = symbols('x1,x2,x3,x4,x5,x6,x7,x8,x9')
			wzs = [x1,x2,x3,x4,x5,x6,x7,x8,x9]
		if len(fc) == 10:
			x1,x2,x3,x4,x5,x6,x7,x8,x9,x10 = symbols('x1,x2,x3,x4,x5,x6,x7,x8,x9,x10')
			wzs = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]
		try:
			r = solve(fc,wzs)
			r = str(r)
			r = r.replace('{','')
			r = r.replace('}','')
			r = r.replace('[','')
			r = r.replace(']','')
			r = r.replace(' ','')
			r = r.replace(',','\n')

			if r.find('(') != -1:
				r = r.replace('(','')
				r = r.replace(')','')
				res = r.splitlines()
				r = ''
				for i in range(1,len(res)+1):
					shu = i%len(fc)
					if shu == 0 :	
						shu = len(fc)	
					if shu == 1 and i//len(fc) >= 1:
						r += '\n或\n'		
					r += 'x'+str(shu)+'='+res[i-1]+'\n'

			if r != '':
				QMessageBox.about(self.ui,'结果',r)
			if r == '':
				QMessageBox.about(self.ui,'结果','无解')
		except:
			QMessageBox.about(self.ui,'警告','方程式不合规')

	def kuozhangongju(self):
		self.kuozhan = kuozhan()
		self.kuozhan.ui.show()



class kuozhan:
	def __init__(self):
		# 从文件中加载UI定义

		# 从 UI 定义中动态 创建一个相应的窗口对象
		self.ui = QUiLoader().load('拓展.ui')

		self.ui.qiudao.clicked.connect(self.fqiudao)
		self.ui.jixian.clicked.connect(self.fjixian)
		self.ui.budingjifen.clicked.connect(self.fbudingjifen)
		self.ui.dingjifen.clicked.connect(self.fdingjifen)

	def fqiudao(self):
		x = symbols('x')
		shizi = self.ui.line1.text()
		try:
			mes = diff(eval(shizi),x)
			self.ui.line1.setText(str(mes))
		except:
			QMessageBox.about(self.ui,'警告','输入不合规')

	def fjixian(self):
		x = symbols('x')
		shu = self.ui.line2.text()
		shizi = self.ui.line3.text()
		try:
			mes = limit(eval(shizi),x,eval(shu))
			self.ui.line3.setText(str(mes))
		except:
			QMessageBox.about(self.ui,'警告','输入不合规')


	def fbudingjifen(self):
		x = symbols('x')
		shizi = self.ui.line4.text()
		try:
			mes = integrate(eval(shizi),x)
			self.ui.line5.setText(str(mes))
		except:
			QMessageBox.about(self.ui,'警告','输入不合规')


	def fdingjifen(self):
		x = symbols('x')
		shang = self.ui.line6.text()
		xia = self.ui.line7.text()
		shizi = self.ui.line8.text()
		try:
			mes = integrate(eval(shizi),(x,eval(xia),eval(shang)))
			self.ui.line9.setText(str(mes))
		except:
			QMessageBox.about(self.ui,'警告','输入不合规')



app = QApplication(sys.argv)
fangchenggongju = fangchenggongju()
fangchenggongju.ui.show()
sys.exit(app.exec_())