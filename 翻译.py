from google_trans_new import google_translator
from PySide2 .QtWidgets import *
from PySide2 .QtGui import *
from PySide2 .QtCore import *
import sys,time

LANGUAGES = {
'zh-cn': 'chinese (simplified)',
'zh-tw': 'chinese (traditional)',
'af': 'afrikaans',
'sq': 'albanian',
'am': 'amharic',
'ar': 'arabic',
'hy': 'armenian',
'az': 'azerbaijani',
'eu': 'basque',
'be': 'belarusian',
'bn': 'bengali',
'bs': 'bosnian',
'bg': 'bulgarian',
'ca': 'catalan',
'ceb': 'cebuano',
'ny': 'chichewa',
'co': 'corsican',
'hr': 'croatian',
'cs': 'czech',
'da': 'danish',
'nl': 'dutch',
'en': 'english',
'eo': 'esperanto',
'et': 'estonian',
'tl': 'filipino',
'fi': 'finnish',
'fr': 'french',
'fy': 'frisian',
'gl': 'galician',
'ka': 'georgian',
'de': 'german',
'el': 'greek',
'gu': 'gujarati',
'ht': 'haitian creole',
'ha': 'hausa',
'haw': 'hawaiian',
'iw': 'hebrew',
'he': 'hebrew',
'hi': 'hindi',
'hmn': 'hmong',
'hu': 'hungarian',
'is': 'icelandic',
'ig': 'igbo',
'id': 'indonesian',
'ga': 'irish',
'it': 'italian',
'ja': 'japanese',
'jw': 'javanese',
'kn': 'kannada',
'kk': 'kazakh',
'km': 'khmer',
'ko': 'korean',
'ku': 'kurdish (kurmanji)',
'ky': 'kyrgyz',
'lo': 'lao',
'la': 'latin',
'lv': 'latvian',
'lt': 'lithuanian',
'lb': 'luxembourgish',
'mk': 'macedonian',
'mg': 'malagasy',
'ms': 'malay',
'ml': 'malayalam',
'mt': 'maltese',
'mi': 'maori',
'mr': 'marathi',
'mn': 'mongolian',
'my': 'myanmar (burmese)',
'ne': 'nepali',
'no': 'norwegian',
'or': 'odia',
'ps': 'pashto',
'fa': 'persian',
'pl': 'polish',
'pt': 'portuguese',
'pa': 'punjabi',
'ro': 'romanian',
'ru': 'russian',
'sm': 'samoan',
'gd': 'scots gaelic',
'sr': 'serbian',
'st': 'sesotho',
'sn': 'shona',
'sd': 'sindhi',
'si': 'sinhala',
'sk': 'slovak',
'sl': 'slovenian',
'so': 'somali',
'es': 'spanish',
'su': 'sundanese',
'sw': 'swahili',
'sv': 'swedish',
'tg': 'tajik',
'ta': 'tamil',
'te': 'telugu',
'th': 'thai',
'tr': 'turkish',
'uk': 'ukrainian',
'ur': 'urdu',
'ug': 'uyghur',
'uz': 'uzbek',
'vi': 'vietnamese',
'cy': 'welsh',
'xh': 'xhosa',
'yi': 'yiddish',
'yo': 'yoruba',
'zu': 'zulu',
}

class Ui_fanyi(QWidget):

	def setupUi(self):
		self.resize(400, 300)
		self.horizontalLayout = QHBoxLayout(self)
		self.horizontalLayout.setSpacing(10)
		self.horizontalLayout.setObjectName(u"horizontalLayout")
		self.horizontalLayout.setContentsMargins(15, 15, 15, 15)
		self.fy = QPlainTextEdit(self)
		self.fy.setObjectName(u"fy")

		self.horizontalLayout.addWidget(self.fy)

		self.verticalLayout = QVBoxLayout()
		self.verticalLayout.setSpacing(10)
		self.verticalLayout.setObjectName(u"verticalLayout")
		self.fpath = QLineEdit(self)
		self.fpath.setObjectName(u"fpath")

		self.verticalLayout.addWidget(self.fpath)

		self.wenjianfanyi = QPushButton(self)
		self.wenjianfanyi.setObjectName(u"wenjianfanyi")

		self.verticalLayout.addWidget(self.wenjianfanyi)

		self.lang = QComboBox(self)
		self.lang.setObjectName(u"lang")

		self.verticalLayout.addWidget(self.lang)

		self.fanyi = QPushButton(self)
		self.fanyi.setObjectName(u"fanyi")

		self.verticalLayout.addWidget(self.fanyi)

		self.jieguo = QCheckBox(self)
		self.jieguo.setObjectName(u"jieguo")

		self.verticalLayout.addWidget(self.jieguo)

		self.verticalLayout.setStretch(0, 10)
		self.verticalLayout.setStretch(1, 10)
		self.verticalLayout.setStretch(2, 10)
		self.verticalLayout.setStretch(3, 10)
		self.verticalLayout.setStretch(4, 10)

		self.horizontalLayout.addLayout(self.verticalLayout)

		self.horizontalLayout.setStretch(0, 4)
		self.horizontalLayout.setStretch(1, 1)

		self.retranslateUi()

		QMetaObject.connectSlotsByName(self)
    # setupUi

	def retranslateUi(self):
		self.setWindowTitle(QCoreApplication.translate("Form", u"\u7ffb\u8bd1", None))
		self.fy.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u8981\u7ffb\u8bd1\u7684\u5185\u5bb9", None))
		self.fpath.setPlaceholderText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u5730\u5740", None))
		self.wenjianfanyi.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u7ffb\u8bd1", None))
		self.fanyi.setText(QCoreApplication.translate("Form", u"\u7ffb\u8bd1", None))
		self.jieguo.setText(QCoreApplication.translate("Form", u"\u7ed3\u679c\u81ea\u52a8\u4fdd\u5b58", None))
    # retranslateUi

class fanyi(QWidget):

	global LANGUAGES
	def __init__(self):
		super().__init__()

		# 主界面
		self.ui = Ui_fanyi()
		self.ui.setupUi()

		self.ui.wenjianfanyi.clicked.connect(self.wjfy)
		self.ui.fanyi.clicked.connect(self.fy)
		self.ui.jieguo.stateChanged.connect(self.jg)
		for key in LANGUAGES.keys():
			self.ui.lang.addItem(LANGUAGES[key])
		self.ui.lang.currentIndexChanged.connect(self.flang)
		self.lang = 'zh-cn'
		self.mod = 0

	def flang(self):
		mlang = self.ui.lang.currentText()
		for key in LANGUAGES.keys():
			if LANGUAGES[key] == mlang:
				self.lang = key

	def fy(self):
		translator = google_translator()
		ytext = self.ui.fy.toPlainText()
		lang_ytext = translator.detect(ytext)
		fytext = translator.translate(ytext, self.lang)
		self.ui.fy.setPlainText(ytext+'\n'+fytext+'\n\n')
		if self.mod == 1:
			with open('C:\\Users\\lenovo\\Desktop\\翻译结果.txt','a',encoding='utf-8') as fout:
				fout.write(str(lang_ytext[1])+'->'+LANGUAGES[self.lang]+'\n'+'原文：'+ytext+'\n'+'译文：'+fytext+'\n\n')
				QMessageBox.about(self.ui,'提示','结果已保存到txt')

	def wjfy(self):
		with open(self.ui.fpath.text(),'r',encoding='utf-8') as f:
			translator = google_translator()
			ytext = f.read()
			lang_ytext = translator.detect(ytext)
			fytext = translator.translate(ytext, self.lang)
			self.ui.fy.setPlainText(ytext+'\n'+fytext+'\n\n')
			if self.mod == 1:
				with open('C:\\Users\\lenovo\\Desktop\\翻译结果.txt','a',encoding='utf-8') as fout:
					fout.write(str(lang_ytext[1])+'->'+LANGUAGES[self.lang]+'\n'+'原文：'+ytext+'\n'+'译文：'+fytext+'\n\n')
					QMessageBox.about(self.ui,'提示','结果已保存到txt')

	def jg(self):
		if self.ui.jieguo.checkState() == Qt.CheckState.Checked:
			self.mod = 1
		if self.ui.jieguo.checkState() == Qt.CheckState.Unchecked:
			self.mod = 0


if __name__ == '__main__':
	app = QApplication(sys.argv)
	cfanyi = fanyi()
	cfanyi.ui.show()
	sys.exit(app.exec_())


