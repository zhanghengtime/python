from numpy import *
import csv
from random import *
import operator
import pymatgen as mg

global pylist
pylist = []
global trees
trees = {}
global dicts
dicts = []

def toFloat(array):  #规范化
    array = mat(array)
    m, n = shape(array)
    newArray = zeros((m, n))
    for i in range(m):
        for j in range(n):
            newArray[i, j] = float(array[i, j])
    return newArray

def dataSet(feature, result): #排序
    dataSet = {}
    for i in range(len(list(feature))):
        dataSet[i] = feature[i]
    dataSet = sorted(dataSet.items(), key=operator.itemgetter(1), reverse=False)  # 降序
    feature = []
    result2 = []
    for i in range(len(dataSet)):
        tuple = dataSet[i]
        feature.append(tuple[1])
        result2.append(result[int(tuple[0])])
    return feature,result2

def loadTrainData():
    l=[]
    with open(r'F:\Testdata\nomad\train.csv') as file:
         lines=csv.reader(file)
         for line in lines:
             l.append(line) #2401*14
    l.remove(l[0])
    l = array(l)
    l = toFloat(l)
    formation_energy_ev_natom = l[:,12]
    bandgap_energy_ev = l[:,13]
    data=l[:,1:]
    return data,formation_energy_ev_natom,bandgap_energy_ev

def loadTestData():
    l=[]
    with open(r'F:\Testdata\nomad\train.csv') as file:
         lines=csv.reader(file)
         for line in lines:
             l.append(line)
    #601*12
    l.remove(l[0])
    l = array(l)
    data = l[:, 1:12]
    return toFloat(data)

def spiltDataSet(dataSet,n_folds): #N份交叉验证
    fold_size=int(len(dataSet)/n_folds)
    dataSet_copy=list(dataSet)
    dataSet_spilt=[]
    for i in range(n_folds):
        fold=[]
        while len(fold) < fold_size:   #这里不能用if，if只是在第一次判断时起作用，while执行循环，直到条件不成立
            index=randrange(len(dataSet_copy))
            fold.append(dataSet_copy.pop(index))  #pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
        dataSet_spilt.append(fold)
    return dataSet_spilt

def get_subsample(dataSet, ratio):
    subdataSet = []
    lenSubdata = round(len(dataSet) * ratio)
    while len(subdataSet) < lenSubdata:
        index = randrange(len(dataSet) - 1)
        subdataSet.append(dataSet[index])
        # print len(subdataSet)
    return subdataSet

def spilt_data(data, loss):
    i = loss[0][1]
    j = loss[0][0]
    data = data[data[:, i].argsort()]
    global pylist
    pylist.append(i)
    #print(pylist)
    data1 = data[0:j+1,:]
    data2 = data[j+1:,:]
    #global trees
    global dicts
    dicts.append(((data1[j,i],i),(data2[0,i],i)))
    print(dicts)
    #trees[(data1[j,i],i)] = 1
    #trees[(data2[0,i],i)] = 0
    return data1, data2

'''def spilt_data2(data, loss):
    global trees
    tree = {}
    i = loss[0][1]
    j = loss[0][0]
    data = data[data[:, i].argsort()]
    global pylist
    pylist.append(i)
    data1 = data[0:j+1,:]
    data2 = data[j+1:,:]
    tree[(data1[j,i],i+0.1)] = 1
    tree[(data2[0,i],i+0.2)] = 0
    for k in trees:
        trees[k] = tree
        break
    return data1, data2'''

'''def spilt_data3(data, loss):
    global trees
    tree = {}
    i = loss[0][1]
    j = loss[0][0]
    data = data[data[:, i].argsort()]
    global pylist
    pylist.append(i)
    data1 = data[0:j+1,:]
    data2 = data[j+1:,:]
    tree[(data1[j,i],i+0.1)] = 1
    tree[(data2[0,i],i+0.2)] = 0
    i = 1
    for k in trees:
        if(i==1):
            continue
        trees[k] = tree
        i = i-1
    return data1, data2'''

def spilt_loss(feature, result):
    feature, result = dataSet(feature,result)
    #print(feature)
    #print(result)
    feature_len = len(feature)
    loss = {}
    for i in range(feature_len):
        c1 = 0.0
        c2 = 0.0
        loss1 = 0.0
        loss2 = 0.0
        for j in range(i+1):
            c1 = c1 + result[j]
        c1 = c1 / (i+1.0)
        for k in range(i+1,feature_len):
            c2 = c2 + result[k]
        if(i==feature_len-1):
            c2 =0
        else:
            c2 = c2 / (feature_len-(i+1.0))
        for j in range(i + 1):
            loss1 = loss1 + (result[j]-c1)**2
        for k in range(i + 1, feature_len):
            loss2 = loss2 + (result[k]-c2)**2
        loss[i] = loss1+loss2
        #print(loss)
    loss = sorted(loss.items(), key=operator.itemgetter(1), reverse=False)  # 降序
    return loss[0]

def get_spilt(data1, data2):
    total_loss = []
    global pylist
    print(pylist)
    for i in range(11):
        if(i in pylist):
            pass
        else:
            s = spilt_loss(data1[:, i], data1[:, 12])
            total_loss.append(s)
        # print(s)
    loss_1 = {}
    for i in range(len(total_loss)):
        loss_1[(total_loss[i][0], i)] = total_loss[i][1]
    loss_1 = sorted(loss_1.items(), key=operator.itemgetter(1), reverse=False)  # 降序
    data11, data22 = spilt_data(data1, loss_1[0])
    get_spilt(data11,data22)
    total_loss = []
    for i in range(11):
        if (i in pylist):
            pass
        else:
            s = spilt_loss(data2[:, i], data2[:, 12])
            total_loss.append(s)
            # print(s)
    loss_1 = {}
    for i in range(len(total_loss)):
        loss_1[(total_loss[i][0], i)] = total_loss[i][1]
    loss_1 = sorted(loss_1.items(), key=operator.itemgetter(1), reverse=False)  # 降序
    data33, data44 = spilt_data(data2, loss_1[0])
    get_spilt(data33,data44)
    return 0

# 选取任意的n个特征，在这n个特征中，选取分割时的最优特征
def get_best_spilt():
    total_loss = []
    data, formation_energy_ev_natom, bandgap_energy_ev = loadTrainData()
    print(data.shape)
    for i in range(11):
        s = spilt_loss(data[:, i], formation_energy_ev_natom)
        total_loss.append(s)
        #print(s)
    loss_1 = {}
    for i in range(len(total_loss)):
        loss_1[(total_loss[i][0],i)] = total_loss[i][1]
    loss_1 = sorted(loss_1.items(), key=operator.itemgetter(1), reverse=False)  # 降序
    data1, data2 = spilt_data(data, loss_1[0])
    get_spilt(data1, data2)
    return 0

def main():
   # data, formation_energy_ev_natom, bandgap_energy_ev = loadTrainData()
   # mat1 = data[data[:, 1].argsort()]
   # print(mat1)
   print(get_best_spilt())
   global trees
   print(dicts)

if __name__ == '__main__':
    main()
