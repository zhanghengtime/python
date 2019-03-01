'''#include <iostream.h>
  #include <math.h>
  void main()  
  {   
    double M[100][100]; 
  double x[100],y[100];  
  double X=1,xx=0,w=1,N=0,P,R=1;  
  int n;   
  cout<<"请输入所求均差阶数："; 
  cin>>n;   
  for(int i=0;i<=n;i++) 
  {  
  cout<<"请输入x"<<i<<"的值："<<endl; 
  cin>>x[i];  
  cout<<"请输入y"<<i<<"的值："<<endl;  
  cin>>y[i];  
  M[i][0]=x[i];
  M[i][1]=y[i];
  }   
  for( int j=2;j<=n+1;j++) 
  {   
  for( i=1;i<=n;i++)  
  {   
  M[i][j]=(M[i][j-1]-M[i-1][j-1])/(M[i][0]-M[i-j+1][0]);  
  } 
  }  
  for(i=1;i<=n;i++)  
  {  
  cout<<"其"<<i<<"阶均差为："<<M[i][i+1]<<endl;  
  } 
   char L;  
  do 
  {  
  double X=1,N=0;P=0;
  cout<<"请输入x的值：x="; 
  cin>>xx;  
  for(i=0;i<n;i++) 
  {  
  X*=xx-x[i];  
  N+=M[i+1][i+2]*X;
  P=M[0][1]+N; 
  }  
  cout<<"其函数值：y="<<P<<endl;   
  cout<<endl<<"如还想算其它插值请按'y'否则按'n'"<<endl;  
  cin>>L; 
  }while(L=='y'); 
  }'''


import numpy as np
import matplotlib.pyplot as plt

M = np.zeros((100,100))
x = np.zeros((100,1))
y = np.zeros((100,1))
X=1
xx=0
w=1
N=0
R=1
x = np.array([0.30,0.42,0.50,0.58,0.66,0.72])
y = np.array([1.04403, 1.08462, 1.11803, 1.15603, 1.19817, 1.23223])
n = int(input("请输入所求均差阶数："))
for i in range(n+1):
    #x[i] = float(input("请输入x"+str(i)+"的值: "))
    #y[i] = float(input("请输入y"+str(i)+"的值："))
    M[i][0]=x[i]
    M[i][1]=y[i]
j=2
while(j <= n+1):
    i = 1
    while(i <= n):
        M[i][j] = (M[i][j - 1] - M[i - 1][j - 1]) / (M[i][0] - M[i - j + 1][0])
        i = i + 1
    j = j + 1
i = 1
while(i<=n):
    print("其"+str(i)+"阶均差为: "+str(M[i][i+1]))
    i= i+1


