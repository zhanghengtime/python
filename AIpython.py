from numpy import *
import csv
import operator

def nomalizing(array):  #正则化
    m, n = shape(array)
    for i in range(m):
        for j in range(n):
            if array[i, j] != 0:
                array[i, j] = 1
    return array

def toInt(array):  #
    array = mat(array)
    m, n = shape(array)
    newArray = zeros((m, n))
    for i in range(m):
        for j in range(n):
            newArray[i, j] = int(array[i, j])
    return newArray

def loadTrainData():
    l=[]
    with open(r'F:\Testdata\digth\train.csv') as file:
         lines=csv.reader(file)
         for line in lines:
             l.append(line) #42001*785
    l.remove(l[0])
    l = array(l)
    label = l[:,0]
    data=l[:,1:]
    return nomalizing(toInt(data)),toInt(label)

def loadTestData():
    l=[]
    with open(r'F:\Testdata\digth\test.csv') as file:
         lines=csv.reader(file)
         for line in lines:
             l.append(line)
    #28001*784
    l.remove(l[0])
    data=array(l)
    return nomalizing(toInt(data))

def classify(inX, dataSet, labels, k):
    inX = mat(inX)                       #转化为矩阵
    dataSet = mat(dataSet)
    labels = mat(labels)
    dataSetSize = dataSet.shape[0]      #读取第一维度的长度
    diffMat = tile(inX, (dataSetSize,1)) - dataSet       #把inX在行上重复dataSetSize次，在列上重复1次
    sqDiffMat = array(diffMat)**2
    sqDistances = sqDiffMat.sum(axis=1)     #以第二维度相加
    distances = sqDistances**0.5          #欧式距离
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[0,sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True) #降序
    return sortedClassCount[0][0]

def saveResult(result):
    with open(r'F:\Testdata\digth\result3.csv','wb') as myFile:
        myWriter = csv.writer(myFile)
        for i in result:
            tmp = []
            tmp.append(i)
            myWriter.writerow(tmp)

def handwritingClassTest():
    trainData,trainLabel = loadTrainData()
    testData = loadTestData()
    m,n = shape(testData)
    resultList=[]
    for i in range(m):
        classifierResult = classify(testData[i], trainData, trainLabel, 5)
        resultList.append(classifierResult)
        print ("the classifier came back with: %d" % (classifierResult))
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
    check()

if __name__ == '__main__':
    main()


