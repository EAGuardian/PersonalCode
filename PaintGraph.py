# 从这里开始是绘制节点demo
from pyecharts import options as opts
from pyecharts.charts import Graph
from math import *
def Circle(r, n):  #求坐标
    l = []
    for i in range(n):
        l.append((r+r*cos(i/n*2*acos(-1)), r+r*sin(i/n*2*acos(-1))))
    return l
def Filter(start,end): #筛选出start到end之间的数据
    file = Reader()
    ffile=[]
    print('start={},end={}'.format(start,end))
    for i in range(len(file)):
        time=float(file[i][0])
        if(time>float(start) and time<float(end)):
            ffile.append(file[i])
    return ffile
def Reader():  #读取文件
    file = []
    with open('./list.txt', 'r') as f:
        for line in f.readlines():
            file.append(list(map(str, line.strip().split(','))))
    return file
def CreateNodes(start,end):  #绘制节点集
    file = Filter(start,end)
    #file = Reader()
    node=[]
    for f in file:
        node.append(f[1])
        node.append(f[3])
    node=list(set(node))  #去重(目前使用该方法会导致排列顺序改变)
    nodes=[]
    pos=Circle(len(node)*10,len(node))
    i=0
    for n in node:
        dir={}
        dir["name"]=n
        dir['x']=pos[i][0]
        dir['y']=pos[i][1]
        i+=1
        dir['symbolSize']=5
        nodes.append(dir)
    return nodes
def CreateLinks(start,end):   #绘制边集
    file = Filter(start,end)
    #file = Reader()
    links=[]
    #首先需要对重复边进行去重处理,边先一ip+','+ip的形式传入列表，去重后再取出
    templist=[]
    for f in file:
        templist.append(f[1]+','+f[3])
    templist=list(set(templist))   #去重(目前使用该方法会导致排列顺序改变)
    for E in templist:
        edge=E.split(',')
        dir = {}
        dir['source']=edge[0]
        dir['target']=edge[1]
        links.append(dir)
    return links

def Paiting(start,end):
    # 从这里是开始绘制节点demo
    nodes = CreateNodes(start,end)
    links = CreateLinks(start,end)
    c = (
        Graph(opts.InitOpts(width='1840px',height='820px'))
            .add("", nodes, links,
                 is_selected=False,
                 is_focusnode=False,
                 layout='none',
                 linestyle_opts=opts.LineStyleOpts(width=2,curve=0.3),
                 edge_symbol={'','arrow'})
            .set_global_opts(title_opts=opts.TitleOpts(title="展示用"))
            .render("graph_base.html")
    )
    # 从这里是结束绘制节点demo