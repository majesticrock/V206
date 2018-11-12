import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def func(x, a, b, c, d):
    return a*x**3 + b*x**2 + c*x + d

werte = csv_read("csv/zeit-temperatur.csv")
xdata = np.zeros(18)
ydata1 = np.zeros(18)
ydata2 = np.zeros(18)
errX = np.zeros(18)
errY1 = np.zeros(18)
errY2 = np.zeros(18)

ignore = True
i=0
for values in werte:
    if(ignore):
        ignore = False
    else:
        xdata[i] = float(values[0])
        ydata1[i] = float(values[2])
        ydata2[i] = float(values[4])
        errX[i] = float(values[1])
        errY1[i] = float(values[3])
        errY2[i] = float(values[5])
        i+=1

x_line = np.linspace(0, 1080)
plt.errorbar(xdata, ydata1, xerr = errX, yerr = errY1, fmt= ".", label="Messwerte T1")
plt.errorbar(xdata, ydata2, xerr = errX, yerr = errY2, fmt = ".", label="Messwerte T2")
popt1, pcov1 = curve_fit(func, xdata, ydata1)
popt2, pcov2 = curve_fit(func, xdata, ydata2)
plt.plot(x_line, func(x_line, *popt1), "r-", label="Fit T1")
plt.plot(x_line, func(x_line, *popt2), "g-", label="Fit T2")

plt.xlabel(r"$t$ / s")
plt.ylabel(r"$T$ / K")

print(popt1)
for i in range(4):
    print(np.sqrt(pcov1[i][i]))
print("\n")
print(popt2)
for i in range(4):
    print(np.sqrt(pcov2[i][i]))

plt.legend()
plt.tight_layout()
plt.savefig("build/plot-t-T.pdf")