import re
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit, QMessageBox
from PySide2.QtUiTools import QUiLoader

sumnum = 0
biao = '''1 氢 H 1.008
2 氦 He 4.0026
3 锂 Li 6.94
4 铍 Be 9.0122
5 硼 B 10.81
6 碳 C 12.011
7 氮 N 14.007
8 氧 O 15.999
9 氟 F 18.998
10 氖 Ne 20.180
11 钠 Na 22.990	
12 镁 Mg 24.305
13 铝 Al 26.982
14 硅 Si 28.085
15 磷 P 30.974
16 硫 S 32.06
17 氯 Cl 35.45
18 氩 Ar 39.95
19 钾 K 39.098
20 钙 Ca 40.078
21 钪 Sc 44.956
22 钛 Ti 47.867
23 钒 V 50.942
24 铬 Cr 51.996
25 锰 Mn 54.938
26 铁 Fe 55.845
27 钴 Co 58.933
28 镍 Ni 58.693
29 铜 Cu 63.546
30 锌 Zn 65.38
31 镓 Ga 69.723
32 锗 Ge 72.63
33 砷 As 74.922
34 硒 Se 78.97
35 溴 Br 79.904
36 氪 Kr 83.798
37 铷 Rb 85.468
38 锶 Sr 87.62
39 钇 Y 88.906
40 锆 Zr 91.224
41 铌 Nb 92.906
42 钼 Mo 95.95
44 钌 Ru 101.07
45 铑 Rh 102.91
46 钯 Pd 106.42
47 银 Ag 107.87
48 镉 Cd 112.41
49 铟 In 114.82
50 锡 Sn 118.71
51 锑 Sb 121.76
52 碲 Te 127.60
53 碘 I 126.90
54 氙 Xe 131.29
55 铯 Cs 132.91
56 钡 Ba 137.33
57 镧 La 138.91
58 铈 Ce 140.12
59 镨 Pr 140.91
60 钕 Nd 144.24
62 钐 Sm 150.36
63 铕 Eu 151.96
64 钆 Gd 157.25
65 铽 Tb 158.93
66 镝 Dy 162.50
67 钬 Ho 164.93
68 铒 Er 167.26
69 铥 Tm 168.93
70 镱 Yb 173.05
71 镥 Lu 174.97
72 铪 Hf 178.49
73 钽 Ta 180.95
74 钨 W 183.84
75 铼 Re 186.21
76 锇 Os 190.23
77 铱 Ir 192.22
78 铂 Pt 195.08
79 金 Au 196.97
80 汞 Hg 200.59
81 铊 Tl 204.38
82 铅 Pb 207.2
'''
D = {}
chulibiao = biao.split()
for i in range(0,len(chulibiao),4):
	D[chulibiao[i+2]] = float(chulibiao[i+3])

class huaxuegongju():

	def __init__(self):
		# 从文件中加载UI定义

		# 从 UI 定义中动态 创建一个相应的窗口对象
		self.ui = QUiLoader().load('化学工具.ui')

		self.ui.button__shiliang.clicked.connect(self.shiliangjisuan)
		self.ui.button__peiping.clicked.connect(self.yanzhengfangchengshipeiping)

	def shiliangjisuan(self):
		global sumnum
		hxs = self.ui.plainTextEdit.toPlainText()

		chuli = re.sub( r"([A-Z])", r" \1", hxs).split()
		for i in range(len(chuli)):
			a = ''
			b = ''
			for c in chuli[i]:
				if c.isalpha():
					a += c
				if c.isnumeric():
					b += c
			if b == '':
				b = 1
			b = int(b)
			if a in D.keys():
				sumnum += D[a]*b
			else:
				QMessageBox.about(self.ui,'计算结果','输入不合规')
				sumnum = ''
				break
		if sumnum != '':
			QMessageBox.about(self.ui,'计算结果','式量：'+str(format(sumnum,'.3f')))

		sumnum = 0

	def yanzhengfangchengshipeiping(self):
		fcs = self.ui.plainTextEdit.toPlainText()
		fy,sc = fcs.split(' = ',1)
		fyhxs = fy.split(' + ')
		schxs = sc.split(' + ')
		chuli2fy = []
		chuli2sc = []
		allyuansu = []
		allthingfy = []
		allthingsc = []
		sumfy = 0
		sumsc = 0
		jieguo = 1

		for i in range(len(fyhxs)):
			thing,fyhxs[i] = fyhxs[i].split(' ',1)
			thing = int(thing)
			allthingfy.append(thing)
			chulify = re.sub( r"([A-Z])", r" \1", fyhxs[i]).split()
			chuli2fy.append({})	
			
			for j in range(len(chulify)):
				a = ''
				b = ''
				for c in chulify[j]:
					if c.isalpha():
						a += c
					if c.isnumeric():
						b += c		
				if b == '':
					b = 1
				b = int(b)
				if chuli2fy[i].__contains__(a):
					chuli2fy[i][a] += b
				else:
					chuli2fy[i][a] = b
					allyuansu.append(a)

		for i in range(len(schxs)):
			thing,schxs[i] = schxs[i].split(' ',1)
			thing = int(thing)
			allthingsc.append(thing)
			chulisc = re.sub( r"([A-Z])", r" \1", schxs[i]).split()
			chuli2sc.append({})	
	
			for j in range(len(chulisc)):
				a = ''
				b = ''
				for c in chulisc[j]:
					if c.isalpha():
						a += c
					if c.isnumeric():
						b += c		
				if b == '':
					b = 1
				b = int(b)
				if chuli2sc[i].__contains__(a):
					chuli2sc[i][a] += b
				else:
					chuli2sc[i][a] = b

		try:
			for i in allyuansu:
				sumfy = 0
				sumsc = 0
				for j in range(len(chuli2fy)):
					if chuli2fy[j].__contains__(i):
						sumfy += chuli2fy[j][i]*allthingfy[j]

				for j in range(len(chuli2sc)):
					if chuli2sc[j].__contains__(i):
						sumsc += chuli2sc[j][i]*allthingsc[j]
				if sumsc != sumfy:
					jieguo = 0
					QMessageBox.about(self.ui,'结果','未配平')
					break
			if jieguo == 1:
				QMessageBox.about(self.ui,'结果','已配平')
		except:
			QMessageBox.about(self.ui,'结果','化学方程式不合规')



app = QApplication([])
huaxuegongju = huaxuegongju()
huaxuegongju.ui.show()
app.exec_()



