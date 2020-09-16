from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
class Ui_mWidget(object):
    def setupUi(self, mWidget):
        mWidget.setObjectName("mWidget")
        mWidget.resize(1000, 600)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(mWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.chooseLayout = QtWidgets.QHBoxLayout()
        self.chooseLayout.setObjectName("chooseLayout")
        self.infoFrame = QtWidgets.QFrame(mWidget)
        self.infoFrame.setStyleSheet("border:1px solid rgb(170,170,170)")
        self.infoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.infoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.infoFrame.setObjectName("infoFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.infoFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.infoLayout = QtWidgets.QVBoxLayout()
        self.infoLayout.setSpacing(6)
        self.infoLayout.setObjectName("infoLayout")
        self.pathLayout = QtWidgets.QHBoxLayout()
        self.pathLayout.setObjectName("pathLayout")
        self.filePathShow = QtWidgets.QLabel(self.infoFrame)
        self.filePathShow.setStyleSheet("")
        self.filePathShow.setObjectName("filePathShow")
        self.pathLayout.addWidget(self.filePathShow)
        self.filePath = QtWidgets.QLineEdit(self.infoFrame)
        self.filePath.setEnabled(False)
        self.filePath.setAcceptDrops(True)
        self.filePath.setReadOnly(False)
        self.filePath.setObjectName("filePath")
        self.pathLayout.addWidget(self.filePath)
        self.infoLayout.addLayout(self.pathLayout)
        self.timeLayout = QtWidgets.QHBoxLayout()
        self.timeLayout.setObjectName("timeLayout")
        self.pointNum = QtWidgets.QLabel(self.infoFrame)
        self.pointNum.setObjectName("pointNum")
        self.timeLayout.addWidget(self.pointNum)
        self.pointNumShow = QtWidgets.QLineEdit(self.infoFrame)
        self.pointNumShow.setEnabled(False)
        self.pointNumShow.setObjectName("pointNumShow")
        self.timeLayout.addWidget(self.pointNumShow)
        self.startTime = QtWidgets.QLabel(self.infoFrame)
        self.startTime.setObjectName("startTime")
        self.timeLayout.addWidget(self.startTime)
        self.startTimeShow = QtWidgets.QLineEdit(self.infoFrame)
        self.startTimeShow.setObjectName("startTimeShow")
        self.timeLayout.addWidget(self.startTimeShow)
        self.endTime = QtWidgets.QLabel(self.infoFrame)
        self.endTime.setObjectName("endTime")
        self.timeLayout.addWidget(self.endTime)
        self.endTimeShow = QtWidgets.QLineEdit(self.infoFrame)
        self.endTimeShow.setEnabled(False)
        self.endTimeShow.setObjectName("endTimeShow")
        self.timeLayout.addWidget(self.endTimeShow)
        self.infoLayout.addLayout(self.timeLayout)
        self.verticalLayout_2.addLayout(self.infoLayout)
        self.chooseLayout.addWidget(self.infoFrame)
        self.btnLayout = QtWidgets.QVBoxLayout()
        self.btnLayout.setObjectName("btnLayout")
        self.sbtnLayout1 = QtWidgets.QHBoxLayout()
        self.sbtnLayout1.setSpacing(20)
        self.sbtnLayout1.setObjectName("sbtnLayout1")
        self.btnOpenFile = QtWidgets.QPushButton(mWidget)
        self.btnOpenFile.setObjectName("btnOpenFile")
        self.sbtnLayout1.addWidget(self.btnOpenFile)
        self.btnStop = QtWidgets.QPushButton(mWidget)
        self.btnStop.setObjectName("btnStop")
        self.sbtnLayout1.addWidget(self.btnStop)
        self.sbtnLayout1.setStretch(0, 1)
        self.sbtnLayout1.setStretch(1, 1)
        self.btnLayout.addLayout(self.sbtnLayout1)
        self.sbtnLayout2 = QtWidgets.QHBoxLayout()
        self.sbtnLayout2.setObjectName("sbtnLayout2")
        self.radio5 = QtWidgets.QRadioButton(mWidget)
        self.radio5.setObjectName("radio5")
        self.sbtnLayout2.addWidget(self.radio5)
        self.radio10 = QtWidgets.QRadioButton(mWidget)
        self.radio10.setChecked(True)
        self.radio10.setObjectName("radio10")
        self.sbtnLayout2.addWidget(self.radio10)
        self.radio20 = QtWidgets.QRadioButton(mWidget)
        self.radio20.setObjectName("radio20")
        self.sbtnLayout2.addWidget(self.radio20)
        self.btnAuto = QtWidgets.QPushButton(mWidget)
        self.btnAuto.setCheckable(False)
        self.btnAuto.setObjectName("btnAuto")
        self.sbtnLayout2.addWidget(self.btnAuto)
        self.btnLayout.addLayout(self.sbtnLayout2)
        self.chooseLayout.addLayout(self.btnLayout)
        self.chooseLayout.setStretch(0, 5)
        self.chooseLayout.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.chooseLayout)
        self.showFrame = QtWidgets.QFrame(mWidget)
        self.showFrame.setStyleSheet("border: 1px solid rgb(200,200,200)")
        self.showFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.showFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.showFrame.setObjectName("showFrame")
        self.verticalLayout_3.addWidget(self.showFrame)
        self.slider = QtWidgets.QSlider(mWidget)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider.setMaximum(28000)
        self.slider.setMinimum(0)
        self.slider.setTickInterval(1000)
        self.slider.setObjectName("slider")
        self.verticalLayout_3.addWidget(self.slider)
        self.verticalLayout_3.setStretch(1, 1)
        self.retranslateUi(mWidget)
        QtCore.QMetaObject.connectSlotsByName(mWidget)

        timer = QTimer()
        timer.timeout.connect(self.Update)
        a = 1.0

        # 进度条变化信号
        self.slider.valueChanged.connect(self.ValChange)
        self.btnAuto.clicked.connect(self.AutoSlider)
        self.btnStop.clicked.connect(self.StopAutoSlider)
        self.btnAuto.clicked.connect(lambda: timer.start(1000))
        self.btnStop.clicked.connect(lambda: timer.stop())

        #绘图
        self.graphGrid = QGridLayout()
        self.browser = QWebEngineView()
        self.graphGrid.addWidget(self.browser)

        import PaintGraph
        PaintGraph.Paiting('0','29000')
        self.browser.load(QUrl(QFileInfo("./graph_base.html").absoluteFilePath()))  # 加载节点图
        self.showFrame.setLayout(self.graphGrid)
    def retranslateUi(self, mWidget):
        _translate = QtCore.QCoreApplication.translate
        mWidget.setWindowTitle(_translate("mWidget", "Demo"))
        self.filePathShow.setText(_translate("mWidget", "文件路径："))
        self.pointNum.setText(_translate("mWidget", "节点数量："))
        self.startTime.setText(_translate("mWidget", "起始时间："))
        self.endTime.setText(_translate("mWidget", "结束时间："))
        self.btnOpenFile.setText(_translate("mWidget", "选择文件"))
        self.btnStop.setText(_translate("mWidget", "停止"))
        self.radio5.setText(_translate("mWidget", "x0.5"))
        self.radio10.setText(_translate("mWidget", "x1.0"))
        self.radio20.setText(_translate("mWidget", "x2.0"))
        self.btnAuto.setText(_translate("mWidget", "自动播放"))

    #获取滚动条速度
    def GetSliderSpeed(self):
        if (self.radio5.isChecked()): return 2.0
        if (self.radio10.isChecked()): return 1.0
        if (self.radio20.isChecked()): return 0.5

    #开始自动播放
    def AutoSlider(self):
        self.radio5.setEnabled(False)
        self.radio10.setEnabled(False)
        self.radio20.setEnabled(False)

    #结束自动播放
    def StopAutoSlider(self):
        self.radio5.setEnabled(True)
        self.radio10.setEnabled(True)
        self.radio20.setEnabled(True)

    # 进度条变化
    def ValChange(self):
        self.startTimeShow.setText(str(self.slider.value()))
        self.endTimeShow.setText(str(self.slider.value() + 1000))
        import PaintGraph
        PaintGraph.Paiting(str(self.slider.value()),str(self.slider.value() + 1000))
        self.browser.load(QUrl(QFileInfo("./graph_base.html").absoluteFilePath()))  # 加载节点图

    #滚动条更新
    def Update(self):
        self.a = self.GetSliderSpeed();
        v = self.slider.value()
        self.slider.setValue(v+1000)


if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    ui=Ui_mWidget()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
