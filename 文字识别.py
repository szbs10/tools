from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import pyautogui,time,win32api,numpy,sys,pytesseract
from PIL import Image


class Ui_wenzi(QWidget):
	def __init__(self):
		super().__init__()
	def setupUi(self):
		self.resize(400, 300)
		self.horizontalLayout_8 = QHBoxLayout(self)
		self.horizontalLayout_8.setSpacing(10)
		self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
		self.horizontalLayout_8.setContentsMargins(15, 15, 15, 15)
		self.wenzi = QPlainTextEdit(self)
		self.wenzi.setObjectName(u"wenzi")

		self.horizontalLayout_8.addWidget(self.wenzi)

		self.verticalLayout = QVBoxLayout()
		self.verticalLayout.setSpacing(10)
		self.verticalLayout.setObjectName(u"verticalLayout")
		self.picpath = QLineEdit(self)
		self.picpath.setObjectName(u"picpath")

		self.verticalLayout.addWidget(self.picpath)

		self.horizontalLayout_6 = QHBoxLayout()
		self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
		self.label = QLabel(self)
		self.label.setObjectName(u"label")

		self.horizontalLayout_6.addWidget(self.label)


		self.verticalLayout.addLayout(self.horizontalLayout_6)

		self.horizontalLayout = QHBoxLayout()
		self.horizontalLayout.setObjectName(u"horizontalLayout")
		self.zuobiao1 = QLineEdit(self)
		self.zuobiao1.setObjectName(u"zuobiao1")

		self.horizontalLayout.addWidget(self.zuobiao1)

		self.zuobiao2 = QLineEdit(self)
		self.zuobiao2.setObjectName(u"zuobiao2")

		self.horizontalLayout.addWidget(self.zuobiao2)

		self.horizontalLayout.setStretch(0, 1)
		self.horizontalLayout.setStretch(1, 1)

		self.verticalLayout.addLayout(self.horizontalLayout)

		self.horizontalLayout_2 = QHBoxLayout()
		self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
		self.jiequ = QPushButton(self)
		self.jiequ.setObjectName(u"jiequ")
		sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.jiequ.sizePolicy().hasHeightForWidth())
		self.jiequ.setSizePolicy(sizePolicy)

		self.horizontalLayout_2.addWidget(self.jiequ)


		self.verticalLayout.addLayout(self.horizontalLayout_2)

		self.horizontalLayout_7 = QHBoxLayout()
		self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
		self.label_2 = QLabel(self)
		self.label_2.setObjectName(u"label_2")

		self.horizontalLayout_7.addWidget(self.label_2)


		self.verticalLayout.addLayout(self.horizontalLayout_7)

		self.horizontalLayout_3 = QHBoxLayout()
		self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
		self.lang = QComboBox(self)
		self.lang.addItem("")
		self.lang.addItem("")
		self.lang.addItem("")
		self.lang.setObjectName(u"lang")
		sizePolicy.setHeightForWidth(self.lang.sizePolicy().hasHeightForWidth())
		self.lang.setSizePolicy(sizePolicy)

		self.horizontalLayout_3.addWidget(self.lang)


		self.verticalLayout.addLayout(self.horizontalLayout_3)

		self.horizontalLayout_4 = QHBoxLayout()
		self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
		self.shibie = QPushButton(self)
		self.shibie.setObjectName(u"shibie")
		sizePolicy.setHeightForWidth(self.shibie.sizePolicy().hasHeightForWidth())
		self.shibie.setSizePolicy(sizePolicy)

		self.horizontalLayout_4.addWidget(self.shibie)


		self.verticalLayout.addLayout(self.horizontalLayout_4)

		self.horizontalLayout_5 = QHBoxLayout()
		self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
		self.shezhi = QPushButton(self)
		self.shezhi.setObjectName(u"shezhi")
		sizePolicy.setHeightForWidth(self.shezhi.sizePolicy().hasHeightForWidth())
		self.shezhi.setSizePolicy(sizePolicy)

		self.horizontalLayout_5.addWidget(self.shezhi)


		self.verticalLayout.addLayout(self.horizontalLayout_5)

		self.verticalLayout.setStretch(0, 1)
		self.verticalLayout.setStretch(1, 1)
		self.verticalLayout.setStretch(2, 1)
		self.verticalLayout.setStretch(3, 1)
		self.verticalLayout.setStretch(4, 1)
		self.verticalLayout.setStretch(5, 1)
		self.verticalLayout.setStretch(6, 1)
		self.verticalLayout.setStretch(7, 1)

		self.horizontalLayout_8.addLayout(self.verticalLayout)

		self.horizontalLayout_8.setStretch(0, 9)
		self.horizontalLayout_8.setStretch(1, 4)

		self.retranslateUi()

		QMetaObject.connectSlotsByName(self)
		# setupUi

	def retranslateUi(self):
		self.setWindowTitle(QCoreApplication.translate("Form", u"\u6587\u5b57\u8bc6\u522b", None))
		self.picpath.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u56fe\u7247\u8def\u5f84", None))
		self.label.setText(QCoreApplication.translate("Form", u"\u5c4f\u5e55\u8bc6\u522b", None))
		self.zuobiao1.setPlaceholderText(QCoreApplication.translate("Form", u"\u5750\u68071", None))
		self.zuobiao2.setPlaceholderText(QCoreApplication.translate("Form", u"\u5750\u68072", None))
		self.jiequ.setText(QCoreApplication.translate("Form", u"\u622a\u53d6", None))
		self.label_2.setText(QCoreApplication.translate("Form", u"\u8bed\u8a00\u9009\u62e9", None))
		self.lang.setItemText(0, QCoreApplication.translate("Form", u"\u82f1\u8bed", None))
		self.lang.setItemText(1, QCoreApplication.translate("Form", u"\u82f1\u8bed+\u7b80\u4f53\u4e2d\u6587", None))
		self.lang.setItemText(2, QCoreApplication.translate("Form", u"\u82f1\u8bed+\u7e41\u4f53\u4e2d\u6587", None))

		self.shibie.setText(QCoreApplication.translate("Form", u"\u8bc6\u522b", None))
		self.shezhi.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
		# retranslateUi



class wenzi(QWidget):

	def __init__(self):
		super().__init__()

		# 主界面
		self.ui = Ui_wenzi()
		self.ui.setupUi()

		self.ui.jiequ.clicked.connect(self.fjq)
		self.ui.shibie.clicked.connect(self.fsb)
		self.ui.shezhi.clicked.connect(self.fsz)
		self.ui.lang.currentIndexChanged.connect(self.flang)

		self.ui.jiequ.setEnabled(False)
		self.ui.shibie.setEnabled(False)

		self.ui.picpath.textChanged.connect(self.check1)
		self.ui.zuobiao1.textChanged.connect(self.check2)
		self.ui.zuobiao2.textChanged.connect(self.check2)

		self.lang = 1
		self.keyzb = ['S','C']

		self.Thread1 = Thread1()
		self.Thread1.start()

		self.mod = 1

	def check1(self):
		text = self.ui.picpath.text()
		text = text.replace(' ','').replace('\n','')
		if text != '':
			self.ui.shibie.setEnabled(True)
		elif text == '':
			self.ui.shibie.setEnabled(False)

	def check2(self):
		text1 = self.ui.zuobiao1.text()
		text2 = self.ui.zuobiao2.text()
		text1 = text1.replace(' ','').replace('\n','')
		text2 = text2.replace(' ','').replace('\n','')
		if text1 != '' and text2 != '' and text1 != text2:
			self.ui.jiequ.setEnabled(True)
		else:
			self.ui.jiequ.setEnabled(False)

	def fjq(self):
		try:
			minx = min(int(self.ui.zuobiao1.text().split(',',1)[0]),int(self.ui.zuobiao2.text().split(',',1)[0]))
			maxx = max(int(self.ui.zuobiao1.text().split(',',1)[0]),int(self.ui.zuobiao2.text().split(',',1)[0]))
			miny = min(int(self.ui.zuobiao1.text().split(',',1)[1]),int(self.ui.zuobiao2.text().split(',',1)[1]))
			maxy = max(int(self.ui.zuobiao1.text().split(',',1)[1]),int(self.ui.zuobiao2.text().split(',',1)[1]))
			if minx != maxx and miny != maxy:
				t = time.time()
				self.ui.hide()
				img = pyautogui.screenshot(f'屏幕截图__工具__{t}.png',region=[minx,miny,maxx-minx,maxy-miny])
				self.ui.picpath.setText(f'屏幕截图__工具__{t}.png')
				self.ui.show()

			else :
				QMessageBox.warning(self.ui,'警告','坐标错误')
		except:
			QMessageBox.warning(self.ui,'警告','坐标错误')

	def fsb(self):
		try:
			picpath = self.ui.picpath.text()
			pic = Image.open(picpath)
			if self.lang == 1:
				wenzi = pytesseract.image_to_string(pic)
			if self.lang == 2:
				wenzi = pytesseract.image_to_string(pic,lang='chi_sim')
			if self.lang == 3:
				wenzi = pytesseract.image_to_string(pic,lang='chi_tra')
			self.ui.wenzi.setPlainText(wenzi)

			if self.mod == 1:
				with open('C:\\Users\\lenovo\\Desktop\\文字识别结果.txt','a',encoding='utf-8') as f:
					f.write(picpath+'\n'+wenzi)
					QMessageBox.about(self.ui,'提示','结果已保存到txt')


		except:
				QMessageBox.warning(self.ui,'警告','路径错误')

	def fsz(self):
		self.shezi = wzshezhi()
		self.shezi.ui.show()
		self.shezi.ui.zuobiaokj.setText('+'.join(cwenzi.keyzb))

	def flang(self):
		lang = self.ui.lang.currentText()

		if lang == '英语':
			self.lang = 1
		if lang == '英语+简体中文':
			self.lang = 2
		if lang == '英语+繁体中文':
			self.lang = 3


class Ui_wzshezhi(QWidget):
	def __init__(self):
		super().__init__()
	def setupUi(self):
		self.resize(146, 204)
		self.verticalLayout = QVBoxLayout(self)
		self.verticalLayout.setSpacing(10)
		self.verticalLayout.setObjectName(u"verticalLayout")
		self.verticalLayout.setContentsMargins(15, 15, 15, 15)
		self.label = QLabel(self)
		self.label.setObjectName(u"label")

		self.verticalLayout.addWidget(self.label)

		self.zuobiaokj = QLineEdit(self)
		self.zuobiaokj.setObjectName(u"zuobiaokj")

		self.verticalLayout.addWidget(self.zuobiaokj)

		self.horizontalLayout = QHBoxLayout()
		self.horizontalLayout.setObjectName(u"horizontalLayout")
		self.zengjia = QPushButton(self)
		self.zengjia.setObjectName(u"zengjia")
		sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.zengjia.sizePolicy().hasHeightForWidth())
		self.zengjia.setSizePolicy(sizePolicy)

		self.horizontalLayout.addWidget(self.zengjia)


		self.verticalLayout.addLayout(self.horizontalLayout)

		self.horizontalLayout_2 = QHBoxLayout()
		self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
		self.shanchu = QPushButton(self)
		self.shanchu.setObjectName(u"shanchu")
		sizePolicy.setHeightForWidth(self.shanchu.sizePolicy().hasHeightForWidth())
		self.shanchu.setSizePolicy(sizePolicy)

		self.horizontalLayout_2.addWidget(self.shanchu)


		self.verticalLayout.addLayout(self.horizontalLayout_2)

		self.jieguo = QComboBox(self)
		self.jieguo.setObjectName(u"jieguo")

		self.verticalLayout.addWidget(self.jieguo)

		self.verticalLayout.setStretch(0, 1)
		self.verticalLayout.setStretch(1, 1)
		self.verticalLayout.setStretch(2, 1)
		self.verticalLayout.setStretch(3, 1)
		self.verticalLayout.setStretch(4, 1)

		self.retranslateUi()

		QMetaObject.connectSlotsByName(self)
    # setupUi

	def retranslateUi(self):
		self.setWindowTitle(QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
		self.label.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u5750\u6807\u5feb\u6377\u952e", None))
		self.zuobiaokj.setText(QCoreApplication.translate("Form", u"S+C", None))
		self.zengjia.setText(QCoreApplication.translate("Form", u"\u589e\u52a0", None))
		self.shanchu.setText(QCoreApplication.translate("Form", u"\u5220\u9664", None))
    # retranslateUi



class wzshezhi(QWidget):

	def __init__(self):
		super().__init__()

		# 主界面
		self.ui = Ui_wzshezhi()
		self.ui.setupUi()

		self.ui.zuobiaokj.returnPressed.connect(self.change)
		self.ui.zengjia.clicked.connect(self.zengjia)
		self.ui.shanchu.clicked.connect(self.shanchu)

		if cwenzi.mod == 1:
			self.ui.jieguo.addItem('结果自动保存txt')
			self.ui.jieguo.addItem('结果不自动保存txt')
		if cwenzi.mod == 0:
			self.ui.jieguo.addItem('结果不自动保存txt')
			self.ui.jieguo.addItem('结果自动保存txt')
			
		self.ui.jieguo.currentIndexChanged.connect(self.jieguo)

	def zengjia(self):
		key,okPressed = QInputDialog.getText(self.ui, "增加","键:",QLineEdit.Normal,'')
		if key in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and key not in cwenzi.keyzb:
			cwenzi.keyzb.append(key)
			self.ui.zuobiaokj.setText('+'.join(cwenzi.keyzb))
		else:
			QMessageBox.warning(self.ui,'警告','增加失败')

	def shanchu(self):
		key,okPressed = QInputDialog.getText(self.ui, "删除","键:",QLineEdit.Normal,'')
		if key in cwenzi.keyzb:
			cwenzi.keyzb.remove(key)
			if cwenzi.keyzb == []:
				cwenzi.keyzb = ['S','C']
				QMessageBox.warning(self.ui,'警告','不能为空')			
			self.ui.zuobiaokj.setText('+'.join(cwenzi.keyzb))
		else:
			QMessageBox.warning(self.ui,'警告','删除失败')

	def change(self):
		text = self.ui.zuobiaokj.text()
		jg = []
		text = text.upper()
		for char in text:
			if char in list('ABCDEFGHIJKLMNOPQRSTUVWXYZ') and char not in jg:
				jg.append(char)
		if jg == []:
			jg = ['S','C']
			self.ui.zuobiaokj.setText('S+C')
		cwenzi.keyzb = jg
		self.ui.zuobiaokj.setText('+'.join(cwenzi.keyzb))


	def jieguo(self):
		if self.ui.jieguo.currentText() == '结果自动保存txt':
			choice = QMessageBox.question(self.ui,'提示','确定要设置为结果自动保存txt吗？')
			if choice == QMessageBox.Yes:
				cwenzi.mod = 1
			if choice == QMessageBox.No:
				cwenzi.mod = 0

		if self.ui.jieguo.currentText() == '结果不自动保存txt':
			choice = QMessageBox.question(self.ui,'提示','确定要设置为结果不自动保存txt吗？')
			if choice == QMessageBox.Yes:
				cwenzi.mod = 0
			if choice == QMessageBox.No:
				cwenzi.mod = 1



class Thread1(QThread):

	def __init__(self):
		super().__init__()

	def run(self):
		while True:
			zbs = []
			mod = 1
			for item in cwenzi.keyzb:
				zb = win32api.GetKeyState(ord(item))
				zbs.append(zb)
			for thing in zbs:
				if thing >= 0:
					mod = 0
			if mod == 1:
				x, y = pyautogui.position()
				if cwenzi.ui.zuobiao1.text() == '':
					cwenzi.ui.zuobiao1.setText(str(x)+','+str(y))
				elif cwenzi.ui.zuobiao2.text() == '':
					cwenzi.ui.zuobiao2.setText(str(x)+','+str(y))
				else :
					cwenzi.ui.zuobiao1.setText(cwenzi.ui.zuobiao2.text())
					cwenzi.ui.zuobiao2.setText(str(x)+','+str(y))

				time.sleep(0.3)




if __name__ == '__main__':
	app = QApplication(sys.argv)
	cwenzi = wenzi()
	cwenzi.ui.show()
	sys.exit(app.exec_())
