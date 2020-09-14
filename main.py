from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget,QFrame, QSplitter, QGridLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt, QUrl, QFileInfo
from PyQt5.QtWebEngineWidgets import QWebEngineView
class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        MainWidget.setObjectName("MainWidget")
        MainWidget.resize(855, 559)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(MainWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ChoiceLayout = QtWidgets.QHBoxLayout()
        self.ChoiceLayout.setObjectName("ChoiceLayout")
        self.Info_frame = QtWidgets.QFrame(MainWidget)
        self.Info_frame.setStyleSheet("border:1px solid rgb(170,170,170)")
        self.Info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Info_frame.setObjectName("Info_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Info_frame)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.InfoLayout = QtWidgets.QVBoxLayout()
        self.InfoLayout.setSpacing(6)
        self.InfoLayout.setObjectName("InfoLayout")
        self.FilePathLayout = QtWidgets.QHBoxLayout()
        self.FilePathLayout.setObjectName("FilePathLayout")
        self.filepathlable = QtWidgets.QLabel(self.Info_frame)
        self.filepathlable.setStyleSheet("")
        self.filepathlable.setObjectName("filepathlable")
        self.FilePathLayout.addWidget(self.filepathlable)
        self.line_fliepath_edit = QtWidgets.QLineEdit(self.Info_frame)
        self.line_fliepath_edit.setEnabled(False)
        self.line_fliepath_edit.setAcceptDrops(True)
        self.line_fliepath_edit.setReadOnly(False)
        self.line_fliepath_edit.setObjectName("line_fliepath_edit")
        self.FilePathLayout.addWidget(self.line_fliepath_edit)
        self.InfoLayout.addLayout(self.FilePathLayout)
        self.NodeInfoLayout = QtWidgets.QHBoxLayout()
        self.NodeInfoLayout.setObjectName("NodeInfoLayout")
        self.pointnum = QtWidgets.QLabel(self.Info_frame)
        self.pointnum.setObjectName("pointnum")
        self.NodeInfoLayout.addWidget(self.pointnum)
        self.pointnum_show = QtWidgets.QLineEdit(self.Info_frame)
        self.pointnum_show.setEnabled(False)
        self.pointnum_show.setObjectName("pointnum_show")
        self.NodeInfoLayout.addWidget(self.pointnum_show)
        self.starttime = QtWidgets.QLabel(self.Info_frame)
        self.starttime.setObjectName("starttime")
        self.NodeInfoLayout.addWidget(self.starttime)
        self.starttime_show = QtWidgets.QLineEdit(self.Info_frame)
        self.starttime_show.setObjectName("starttime_show")
        self.NodeInfoLayout.addWidget(self.starttime_show)
        self.endtime = QtWidgets.QLabel(self.Info_frame)
        self.endtime.setObjectName("endtime")
        self.NodeInfoLayout.addWidget(self.endtime)
        self.endtime_show = QtWidgets.QLineEdit(self.Info_frame)
        self.endtime_show.setEnabled(False)
        self.endtime_show.setObjectName("endtime_show")
        self.NodeInfoLayout.addWidget(self.endtime_show)
        self.InfoLayout.addLayout(self.NodeInfoLayout)
        self.verticalLayout_2.addLayout(self.InfoLayout)
        self.ChoiceLayout.addWidget(self.Info_frame)
        self.ChooseFileBtn = QtWidgets.QPushButton(MainWidget)
        self.ChooseFileBtn.setObjectName("ChooseFileBtn")
        self.ChoiceLayout.addWidget(self.ChooseFileBtn)
        self.RefreshBtn = QtWidgets.QPushButton(MainWidget)
        self.RefreshBtn.setObjectName("RefreshBtn")
        self.ChoiceLayout.addWidget(self.RefreshBtn)
        self.verticalLayout_3.addLayout(self.ChoiceLayout)
        self.Show_frame = QtWidgets.QFrame(MainWidget)
        self.Show_frame.setStyleSheet("border: 1px solid rgb(200,200,200)")
        self.Show_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Show_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Show_frame.setObjectName("Show_frame")
        #图的框架设置
        self.Graph_grid = QGridLayout()     #栅格布局
        self.Browser = QWebEngineView()     #浏览器
        self.Graph_grid.addWidget(self.Browser)   #增加浏览器窗口
        self.Show_frame.setLayout(self.Graph_grid)   #设置展示框的栅格布局
        self.verticalLayout_3.addWidget(self.Show_frame)
        self.Slider = QtWidgets.QSlider(MainWidget)
        self.Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Slider.setTickInterval(5)
        self.Slider.setObjectName("Slider")
        self.verticalLayout_3.addWidget(self.Slider)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)
        self.retranslateUi(MainWidget)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)
        # 从这里开始是绘制节点demo
        from pyecharts import options as opts
        from pyecharts.charts import Graph
        nodes = [
            {"name": "结点1", "symbolSize": 20},
            {"name": "结点2", "symbolSize": 20},
            {"name": "结点3", "symbolSize": 20},
            {"name": "结点4", "symbolSize": 20},
            {"name": "结点5", "symbolSize": 20},
            {"name": "结点6", "symbolSize": 20},
            {"name": "结点7", "symbolSize": 20},
            {"name": "结点8", "symbolSize": 20},
        ]
        links = []
        for i in nodes:
            for j in nodes:
                links.append({"source": i.get("name"), "target": j.get("name")})
        c = (
            Graph()
                .add("", nodes, links, repulsion=4000, edge_symbol={"arrow"})
                .set_global_opts(title_opts=opts.TitleOpts(title="Graph-Demo"))
                .render("graph_base.html")
        )
        # 从这里是结束绘制节点demo
        self.Browser.load(QUrl(QFileInfo("./graph_base.html").absoluteFilePath()))  # 加载节点图
    def retranslateUi(self, MainWidget):
        _translate = QtCore.QCoreApplication.translate
        MainWidget.setWindowTitle(_translate("MainWidget", "Demo"))
        self.filepathlable.setText(_translate("MainWidget", "文件路径："))
        self.pointnum.setText(_translate("MainWidget", "节点数量："))
        self.starttime.setText(_translate("MainWidget", "起始时间："))
        self.endtime.setText(_translate("MainWidget", "结束时间："))
        self.ChooseFileBtn.setText(_translate("MainWidget", "选择文件"))
        self.RefreshBtn.setText(_translate("MainWidget", "刷新"))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    ui = Ui_MainWidget()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())