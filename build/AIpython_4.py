from numpy import *
import csv
import operator

global pylist
pylist = []
global trees
trees = {}

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
    dataSet = sorted(dataSet.items(), key=operator.itemgetter(1), reverse=False)  # 升序
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

def rspilt_data(data, loss): #分割数据 右树
    i = loss[1]  #分割特征
    j = loss[0]  #分割位置
    data = data[data[:, i].argsort()]
    global pylist
    global trees
    pylist.append(i)
    data1 = data[0:j+1,:]
    data2 = data[j+1:,:]
    print(data1[j, i])
    if (not trees):
        trees[(data1[j, i], i+0.1)] = 0
        trees[(data1[0, i], i+0.2)] = 1
    else:
        for k in trees:
            if(trees[k] == 1):
                trees[k] = {(data1[j,i],i):0,(data1[0,i],i):1}
    return data1, data2

def lspilt_data(data, loss): #分割数据
    i = loss[1]  # 分割特征
    j = loss[0]  # 分割位置
    print(i)
    data = data[data[:, i].argsort()]
    global pylist
    global trees
    pylist.append(i)
    data1 = data[0:j + 1, :]
    data2 = data[j + 1:, :]
    if (not trees):
        trees[(data1[j, i], i)] = 0
        trees[(data1[0, i], i)] = 1
    else:
        for k in trees:
            if (trees[k] == 0):
                trees[k] = {(data1[j, i], i): 0, (data1[0, i], i): 1}
    return data1, data2

def spilt_loss(feature, result , num): #num代表分割特征
    feature, result = dataSet(feature,result)
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
        loss[(i,num)] = loss1+loss2
    loss = sorted(loss.items(), key=operator.itemgetter(1), reverse=False)  # 升序
    print(loss[0])
    return loss[0]   #(分割点，损失)

def get_spilt(data1, data2):
    total_loss = []
    global pylist
    print(pylist)
    for i in range(11):
        if(i in pylist):
            pass
        else:
            s = spilt_loss(data1[:, i], data1[:, 11], i)
            total_loss.append(s)
    loss_1 = {}
    for k in range(len(total_loss)):
        loss_1[total_loss[k][0]] = total_loss[k][1]
    loss_1 = sorted(loss_1.items(), key=operator.itemgetter(1), reverse=False)  # 升序
    print(loss_1)
    data11, data22 = lspilt_data(data1, loss_1[0][0])
    get_spilt(data11,data22)
    total_loss = []
    for i in range(11):
        if (i in pylist):
            pass
        else:
            s = spilt_loss(data2[:, i], data2[:, 11],i)
            total_loss.append(s)
    loss_1 = {}
    for i in range(len(total_loss)):
        loss_1[(total_loss[i][0], i)] = total_loss[i][1]
    loss_1 = sorted(loss_1.items(), key=operator.itemgetter(1), reverse=False)  # 升序
    data33, data44 = rspilt_data(data2, loss_1[0])
    get_spilt(data33,data44)
    return 0

# 选取任意的n个特征，在这n个特征中，选取分割时的最优特征
def get_best_spilt():
    total_loss = []
    data, formation_energy_ev_natom, bandgap_energy_ev = loadTrainData()
    for i in range(11):
        s = spilt_loss(data[:, i], formation_energy_ev_natom, i)
        total_loss.append(s)
    loss_1 = {}
    for k in range(len(total_loss)):
        loss_1[total_loss[k][0]] = total_loss[k][1]
    loss_1 = sorted(loss_1.items(), key=operator.itemgetter(1), reverse=False)  # 升序
    print(loss_1)
    data1, data2 = rspilt_data(data, loss_1[0][0])
    get_spilt(data1, data2)
    return 0

def main():
   print(get_best_spilt())
   global trees
   print(trees)

if __name__ == '__main__':
    main()

