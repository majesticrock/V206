import numpy as np 
import math
import pandas as pd
import uncertainties.unumpy as unp
import matplotlib.pyplot as plt
#####Für die Berechnung der linearen Regression (zu L)
df=pd.read_csv('csv/temppascal.csv', sep=';', header =None)
#print(df.values)
u = df.values[:,0]
#du = df.values[:,1]
#fu = unp.uarray(u,du)
#print(fu)
i = df.values[:,1]
#di = df.values[:,3]
#off = df.values[:,4]
#i = i - off
#i = i 
#fi = unp.uarray(i,di)
#print(fi)
x_m = np.mean(i)
y_m = np.mean(u)
#print(x_m)
#print(y_m)
#dx_m = unp.std_devs(fi) / unp.sqrt(len(i))
#dy_m = unp.std_devs(fu) / unp.sqrt(len(u))


dx_m = np.std(i, ddof=1) / np.sqrt(len(i))



dy_m = np.std(u, ddof=1) / np.sqrt(len(u))

print(dx_m)
print(dy_m)

b = (np.sum((i-x_m) * (u-y_m) ) ) / np.sum((i-x_m)**2)
print(b)
a = y_m - b * x_m
print(a)
i = i / 1000
p = u * i 
ra = u/i 
#(p)
#print(ra)

 