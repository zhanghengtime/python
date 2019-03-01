'''
//拉格朗日插值
#include<iostream>
using namespace std;
void main(){
	 double x[5],y[5],a[3],b[3];//三个数组分别存放的是节点的横坐标，纵坐标，以及所求点的横坐标和对应的结果
	 double n,m;//三个变量分别存放的是分子，分母
	 int c,d,e,k;//三个数组的输入计数以及lk（x）的k

	//输入三个数组
	 cout<<"输入横坐标"<<endl;
	 for(c=0;c<=4;c++){
		cin>>x[c];
	}
	 cout<<"输入纵坐标"<<endl;
	 for(d=0;d<=4;d++){
	 	cin>>y[d];
	}
	 cout<<"输入所求点的横坐标"<<endl;
	 for(e=0;e<=2;e++){
		cin>>a[e];
	}

	 for(e=0;e<=2;e++){//计算三个数的函数值
		for(k=0;k<=4;k++){//计算lk（x）
			n=1.0;
			m=1.0;
			for(c=0;c<=4;c++){
				if(k!=c){
				n*=a[e]-x[c];
				m*=x[k]-x[c];
				}
				b[e]=y[k]*n/m;
			}
		}
		cout<<'b'<<'['<<e<<']'<<'='<<b[e]<<endl;
	}
}
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
x, y, a, b = [-3.0,-1.0,1.0,2.0,3.0], [1.0,1.5,2.0,2.0,1.0], [-2,0,2.75], []
bc = []
cc = np.arange(-3.0, 3, 0.005)
'''for e in range(5):
    x.append(float(input("输入横坐标:" )))
for f in range(5):
    y.append(float(input("输入纵坐标:" )))
for g in range(3):
    a.append(float(input("输入所求点的横坐标:")))'''
e = 0
while(e<=2):
    k = 0
    yy = 0.0
    while(k<=4):
        n = 1.0
        m = 1.0
        c = 0
        while(c<=4):
            if(k!=c):
                n = n * (a[e]-x[c])
                m = m * (x[k]-x[c])
            c = c + 1
        yy = yy + y[k] * (n / m)
        k = k + 1
    b.append(yy)
    print("b[%.0f]=%f" % (e, b[e]))
    e = e + 1

e = 0
while(e<=len(cc)-1):
    k = 0
    yy = 0.0
    while(k<=4):
        n = 1.0
        m = 1.0
        c = 0
        while(c<=4):
            if(k!=c):
                n = n * (cc[e]-x[c])
                m = m * (x[k]-x[c])
            c = c + 1
        yy = yy + y[k] * (n / m)
        k = k + 1
    bc.append(yy)
    e = e + 1

plt.figure("图像")
plt.title('拉格朗日插值法', fontproperties='SimHei')
plt.plot(a, b,'gX')
plt.plot(cc,bc,'r')
plt.ylabel('y')
plt.xlabel('x')
plt.show()




'''import numpy as np
count_sum = 0
i = 1
while(i<=10000):
    count_sum = np.array(count_sum + (1/pow(i,2))).astype(np.float32)
    i = i + 1
print("count_sum = %f" % count_sum)
count_sum = 0
i = 10000
while(i >= 1 ):
    count_sum = np.array(count_sum + (1 / pow(i,2)))
    i = i - 1
print("count_sum = %f" % count_sum)'''

