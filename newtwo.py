'''from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

data = load_iris()
features = data['data']
features_names = data['feature_names']
target = data['target']
for t, marker, c in zip(range(3),">ox","rgb"):
    plt.scatter(features[target == t,0],
                features[target == t,1],
                marker=marker, c=c)
plt.show()
#features = features[~is_setosa]
#labels = labels[~is_setosa]
plength = features[:, 2]
is_setosa = (labels == 'setosa')
max_setosa = plength[is_setosa].max()
min_non_setosa = plength[~is_setosa].min()
print('Maximum of setosa: {0}.'.format(max_setosa))
print('Minimum of others: {0}.'.format(min_non_setosa))'''

'''import numpy as np
from sklearn.datasets import load_iris  # 如果安装的是anaconda的话会自带
from matplotlib import pyplot as plt  # 或者import matplotlib.pyplot as plt

data = load_iris()  # 直接装载iris数据集
features = data['data']  # 或者features = data.data（这即可以作为字典的键索取，也被定为该变量的属性）
feature_names = data['feature_names']
target = data['target']

# 下面是画出6个子图的部分
pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
for i, (p0, p1) in enumerate(pairs):  # enumerate函数在《howto-functional》中有介绍
    plt.subplot(2, 3, i + 1)
    for t, marker, c in zip(range(3), ">ox", "rgb"):
        plt.scatter(features[target == t, p0], features[target == t, p1], marker=marker, c=c)
    plt.xlabel(feature_names[p0])
    plt.ylabel(feature_names[p1])
    plt.xticks([])
    plt.yticks([])
plt.show()'''

'''import numpy as np
from sklearn.datasets import load_iris

data = load_iris()
features = data['data']  # 读取特征矩阵
labels = data['target_names'][data['target']]  # 即name[target]，两个都是numpy.ndarray类型

plength = features[:, 2]  # 肉眼观察可以直接区分的特征
is_setosa = (labels == 'setosa')  # 生成标签等于‘setosa’的bool索引矩阵
print('Maximum of setosa: {0}.'.format(plength[is_setosa].max()))  # 输出setosa的最大上限
print('Minimum of others: {0}.'.format(plength[~is_setosa].min()))  # 输出其他两类的最小下限*/

from matplotlib import pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from threshold import learn_model, apply_model, accuracy  # 从阈值模块中装载模型学习，使用，测试函数

data = load_iris()  # 装载数据
features = data['data']  # 读取特征部分
labels = data['target_names'][data['target']]  # 将【0 1 2】标签换成名称

setosa = (labels == 'setosa')  # 生成bool索引矩阵
features = features[~setosa]  # 提取其余两类特征
labels = labels[~setosa]  # 提取其余两类标签
virginica = (labels == 'virginica')  # 读取两类中为virginica的标签

testing = np.tile([True, False], 50)  # 创建布尔矩阵，其中为【true，false，true，false...】一共50对
training = ~testing  # 上面取反，这样就是间隔的将一个做训练数据，一个测试

model = learn_model(features[training], virginica[training])  # 使用写好的模型训练函数
train_error = accuracy(features[training], virginica[training], model)  # 模型测试训练集的正确率
test_error = accuracy(features[testing], virginica[testing], model)'''



#print('''''\
#Training error was {0:.1%}.
#Testing error was {1:.1%} (N = {2}).
#'''.format(train_error, test_error, testing.sum())

import math
print("{:.10f}".format(math.pi * 2.0 * 2.0))


