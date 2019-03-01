"""import turtle

def drawSnake(red, angle, len, neckrad):
    for i in range(len):
        turtle.circle(red, angle)    #circle函数画一个半径为red的圆,angle弧度值
        turtle.circle(-red, angle)
    turtle.circle(red, angle/2)
    turtle.fd(red)               #运行距离
    turtle.circle(neckrad+1 ,180)
    turtle.fd(red*2/3)

def main():
    turtle.setup(1500, 800, 0, 0)   #启动图形窗口 参数 长，宽，左上角位置
    pythonsize = 30
    turtle.pensize(30)             #运行轨迹的宽度
    turtle.pencolor('blue')         #颜色 blue
    turtle.speed(1)
    turtle.seth(-40)                #启动时运行的方向
    drawSnake(40,80,6,pythonsize/2)

if __name__ == '__main__':
    main()"""

'''
import sys
print(sys.float_info)
print(len(str(pow(2,pow(2,20)))))
z = 1.23e-4+5.6e+89j
print(z.imag)
'''

#1
'''str1 = input('请输入一个人的名字: ')
str2 = input('请输入一个国家名字: ')
print('世界那么大，{0}想去{1}看看。'.format(str1,str2))
'''

#2
'''n = input('please input a number: ')
s = 0
for i in range(int(n)):
    s += i+1
print(s)'''

#3
'''for i in range(1,10):
    for s in range(1,i+1):
        print(str(i) + '*' + str(s) + '=' + str(i*s),end=' ')
    print('')

for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={:2}'.format(j,i,i*j),end=' ')
    print('')'''

#4
'''sum = 1
summ = 0
for i in range(1,10):
    sum *= i
    summ += sum
print(summ)'''


#5
'''sum = 1
for i in range(5):
    sum = (sum + 1) * 2
print(sum)'''

#6
'''diets = []
diet = ['白菜','牛肉','菠菜','辣椒','葱']
for i in diet:
    for j in diet:
        if i != j:
            food = []
            food.append(i)
            food.append(j)
    diets.append(food)
    for k in diet:
        for g in diet:
            if k != g != i:
                food = []
                food.append(k)
                food.append(g)
                food.append(i)
    diets.append(food)
print (diets)'''


#7
'''import turtle

def main():
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.speed(1)
    while True:
        turtle.forward(200)
        turtle.right(144)
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()
if __name__ == '__main__':
    main()'''


#8
'''import turtle

turtle.color('red','yellow')
turtle.begin_fill()
turtle.speed(9)
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.pos()) < 1:
        break
turtle.end_fill()
turtle.done()'''


#9
'''from random import random
from math import sqrt
from time import clock

DATAS = 1200000
hits = 0
clock()
for i in range(1,DATAS):
    x,y = random() ,random()
    dist = sqrt(x**2 + y**2)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/DATAS)
print("PI is %s" % pi)
print('time is %-5.5ss' % clock())
'''


#10
'''import requests
url  = 'https://www.amazon.cn/gp/product/B002BVK1Z0'
try:
    kv = {'User-Agent':'Mozilla/5.0'}
    r = requests.get(url,headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print('爬取失败！')
'''

#11
'''import requests
url  = "http://www.baidu.com/s"
try:
    kv = {'User-Agent':'Mozilla/5.0'}
    key = {'wd':'Python'}
    r = requests.get(url,headers=kv, params = key)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(len(r.text))
    print(r.request.url)
    #print(r.text)
except:
    print('爬取失败！')'''


#12
'''import requests
import os
url  = "https://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"
root = "D://pics//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb+') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print('文件已存在 ')
except:
    print('爬取失败！')'''


#13
'''import turtle
import time
turtle.hideturtle()
turtle.speed(1)
turtle.fillcolor('red')
turtle.begin_fill()
for i in range(5):
    turtle.forward(200)
    turtle.right(144)
turtle.end_fill()
time.sleep(5)'''

'''import turtle
import time
turtle.speed(10)
turtle.pensize(2)
for x in range(100):
    turtle.forward(2*x)
    turtle.left(90)
time.sleep(10)'''

'''import turtle
import time
turtle.pensize(2)
turtle.bgcolor("black")
colors = ["red", "yellow",'purple','blue']
turtle.tracer(False)
for x in range(400):
    turtle.forward(2*x)
    turtle.color(colors[x % 4])
    turtle.left(91)
turtle.tracer(True)
time.sleep(5)'''

'''from turtle import Turtle

def tree(plist, l, a, f):
    if l > 5:
        lst = []
        for p in plist:
            p.forward(l)
            q = p.clone()
            p.left(a)
            q.right(a)
            lst.append(p)
            lst.append(q)
        tree(lst, l * f, a, f)

def main():
    p = Turtle()
    p.color('green')
    p.pensize(5)
    p.hideturtle()
    p.speed(10)
    p.left(90)
    p.penup()
    p.goto(0,-300)
    p.pendown()
    t = tree([p],250,65,0.6375)

main()'''


#14
import turtle
import time

turtle.title('数据驱动的动态路径绘制')
turtle.setup(800,600,0,0)

pen = turtle.Turtle()
pen.color('red')
pen.width(5)
pen.shape('turtle')
pen.speed(2)
pen.right(36)
result = []
file = open('datacolor.txt', 'r')
for line in file:
    result.append(list(map(float,line.split(','))))
print(result)
for i in range(len(result)):
    pen.color((result[i][3],result[i][4],result[i][5]))
    pen.fd(result[i][0])
    if result[i][1]:
        pen.rt(result[i][2])
    else:
        pen.lt(result[i][2])
#pen.goto(0,0)
pen.hideturtle()
time.sleep(10)























