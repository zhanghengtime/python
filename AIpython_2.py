from numpy import *
import csv
from decimal import Decimal
from operator import *
import operator

def nomalizing(array):  #正则化
    m, n = shape(array)
    for i in range(m):
        for j in range(n):
            if array[i, j] != 0:
                array[i, j] = array[i, j]
    return array

def toInt(array):
    array = mat(array)
    m, n = shape(array)
    newArray = zeros((m, n))
    for i in range(m):
        for j in range(n):
            newArray[i, j] = float(array[i, j])
            while(newArray[i,j]>1):
               newArray[i,j] = newArray[i,j] / 10.0
            '''while(newArray[i,j]<0.1):
                if(newArray[i,j] == 0):
                    break
                newArray[i,j] = newArray[i,j] * 10'''
    return newArray

def toFloat(array):
    array = mat(array)
    m, n = shape(array)
    newArray = zeros((m, n))
    for i in range(m):
        for j in range(n):
            newArray[i, j] = float(array[i, j])
    return newArray

def loadTrainData():
    l=[]
    with open(r'F:\Testdata\nomad\train.csv') as file:
         lines=csv.reader(file)
         for line in lines:
             l.append(line) #2401*14
    l.remove(l[0])
    l = array(l)
    formation_energy_ev_natom = l[:,12]
    bandgap_energy_ev = l[:,13]
    label = l[:,0]
    data=l[:,1:11]
    return nomalizing(toInt(data)),toFloat(label),toFloat(formation_energy_ev_natom),toFloat(bandgap_energy_ev)

def loadTestData():
    l=[]
    with open(r'F:\Testdata\nomad\test.csv') as file:
         lines=csv.reader(file)
         for line in lines:
             l.append(line)
    #601*12
    l.remove(l[0])
    l = array(l)
    label = l[:, 0]
    data = l[:, 1:11]
    return nomalizing(toInt(data)), toFloat(label)

def classify(inX, dataSet, formation_energy, bandgap_energy, k):
    inX = mat(inX)                       #转化为矩阵
    dataSet = mat(dataSet)
    formation_energy = mat(formation_energy)
    bandgap_energy = mat(bandgap_energy)
    dataSetSize = dataSet.shape[0]      #读取第一维度的长度
    diffMat = tile(inX, (dataSetSize,1)) - dataSet       #把inX在行上重复dataSetSize次，在列上重复1次
    sqDiffMat = array(diffMat)**2
    sqDistances = sqDiffMat.sum(axis=1)     #以第二维度相加
    distances = sqDistances**0.5          #欧式距离
    sortedDistIndicies = distances.argsort()
    classCount1 = {}
    classCount2 = {}
    voteIformation_energy = 0.0
    voteIbandgap_energy = 0.0
    for i in range(k):
        voteIformation_energy = formation_energy[0,sortedDistIndicies[i]] + voteIformation_energy
        voteIbandgap_energy = bandgap_energy[0,sortedDistIndicies[i]] +  voteIbandgap_energy
        classCount1[voteIformation_energy] = classCount1.get(voteIformation_energy,0) + 1
        classCount2[voteIformation_energy] = classCount2.get(voteIformation_energy,0) + 1
    sortedClassCount1 = sorted(classCount1.items(), key=operator.itemgetter(1), reverse=True) #降序
    sortedClassCount2 = sorted(classCount2.items(), key=operator.itemgetter(1), reverse=True)  # 降序
    voteIformation_energy = voteIformation_energy / k / 1.0
    voteIbandgap_energy = voteIbandgap_energy / k / 1.0
    return voteIformation_energy, voteIbandgap_energy

def saveResult(result):
    with open(r'F:\Testdata\nomad\result.csv','w',newline='') as myFile:
        myWriter = csv.writer(myFile)
        k = 0
        for i in result:
            tmp = []
            tmp.append(i)
            myWriter.writerow(tmp)

def handwritingClassTest():
    trainData,trainLabel,formation_energy_ev_natom,bandgap_energy_ev = loadTrainData()
    testData,testLabel = loadTestData()
    m,n = shape(testData)
    resultList=[]
    for i in range(m):
        classifierResult1,classifierResult2 = classify(testData[i], trainData, formation_energy_ev_natom, bandgap_energy_ev,13) #11为最佳
        classifierResult1 = Decimal(str(classifierResult1)).quantize(Decimal('0.000000'))
        classifierResult2 = Decimal(str(classifierResult2)).quantize(Decimal('0.000000'))
        resultList.append([float(classifierResult1),float(classifierResult2)])
    saveResult(resultList)

def check():
    trainDatacheck, trainLabelcheck = loadTrainData()
    m, n = shape(trainDatacheck)
    i, j = shape(trainLabelcheck)
    m  = int(m / 4.0)
    j = int(j / 4.0)
    trainData = trainDatacheck[m:,:]
    trainLabel = trainLabelcheck[:,j:]
    testData = trainDatacheck[0:m,:]
    testLabel = trainLabelcheck[:,0:j]
    print(shape(testData))
    print(shape(testLabel))
    mm, nn = shape(testData)
    errorCount = 0
    ZhCount = 1
    for i in range(mm):
        classifierResult = classify(testData[i], trainData, trainLabel, 7)
        print ("the classifier came back with: %d, the real answer is: %d  , the count is %d" % (classifierResult, testLabel[0, i], ZhCount))
        if (classifierResult != testLabel[0, i]): errorCount += 1.0
        if(ZhCount % 100 == 0): print ("the classifier came back with: %d, the real answer is: %d  , the count is %d" % (classifierResult, testLabel[0, i], ZhCount))
        ZhCount = ZhCount + 1
    print("\nthe total number of errors is: %d" % errorCount)
    print("\nthe total error rate is: %f" % (errorCount / float(mm)))

def main():
    handwritingClassTest()
    check()


if __name__ == '__main__':
    main()



