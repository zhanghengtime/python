import scipy as sp
import matplotlib.pyplot as plt

def error(f, x, y):
    return sp.sum((f(x) - y)**2)

data = sp.genfromtxt(r"D:\anaconda\data\web_traffic.tsv",delimiter="\t")
x = data[:,0]
y = data[:,1]
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]
inflection = int(3.5*7*24)
xa = x[:inflection]
ya = y[:inflection]
xb = x[inflection:]
yb = y[inflection:]
fa = sp.poly1d(sp.polyfit(xa, ya, 1))
fb = sp.poly1d(sp.polyfit(xb, yb, 1))
fa_error = error(fa, xa, ya)
fb_error = error(fb, xb, yb)
print("Error inflection=%f" % (fa_error + fb_error))
fp1, residuals, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)
fp2 = sp.polyfit(x, y, 2)
fp3 = sp.polyfit(x, y, 3)
fp4 = sp.polyfit(x, y, 10)
fp5 = sp.polyfit(x, y, 15)
f1 = sp.poly1d(fp1)
f2 = sp.poly1d(fp2)
f3 = sp.poly1d(fp3)
f4 = sp.poly1d(fp4)
f5 = sp.poly1d(fp5)
plt.scatter(x,y)
plt.title('wed traffic over the last month')
plt.xlabel('Time')
plt.ylabel('Hits/hour')
plt.xticks([w*7*24 for w in range(10)], ['week %i' %w for w in range(10)])
fx = sp.linspace(0, x[-1], 1000)
l1, = plt.plot(fx, f1(fx), linewidth=4 , color='green')
l2, = plt.plot(fx, f2(fx), linewidth=4 , color='red')
l3, = plt.plot(fx, f3(fx), linewidth=4 , color='black')
l4, = plt.plot(fx, f4(fx), linewidth=4 , color='yellow')
l5, = plt.plot(fx, f5(fx), linewidth=4 , color='pink')
plt.legend([l1, l2, l3, l4, l5], ["d=%i" % f1.order,"d=%i" % f2.order,"d=%i" % f3.order, "d=%i" % f4.order, "d=%i" % f5.order], loc = 'upper left')
plt.autoscale(tight=True)
plt.grid
plt.show()