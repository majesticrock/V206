import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def func(x, a, b, c):
    return a*x**2 + b*x + c

werte = csv_read("csv/zeit-temperatur.csv")
xdata = np.zeros(18)
ydata1 = np.zeros(18)
ydata2 = np.zeros(18)

ignore = True
i=0
for values in werte:
    if(ignore):
        ignore = False
    else:
        xdata[i] = float(values[0])
        ydata1[i] = float(values[2])
        ydata2[i] = float(values[4])
        i+=1

x_line = np.linspace(0, 1080)
plt.plot(xdata, ydata1, "y+", label="Messwerte T1")
plt.plot(xdata, ydata2, "b+", label="Messwerte T2")
popt1, pcov1 = curve_fit(func, xdata, ydata1)
popt2, pcov2 = curve_fit(func, xdata, ydata2)
plt.plot(x_line, func(x_line, *popt1), "r-", label="Fit T1")
plt.plot(x_line, func(x_line, *popt2), "g-", label="Fit T2")

plt.xlabel(r"$t$ / s")
plt.ylabel(r"$T$ / K")

plt.legend()
plt.tight_layout()
plt.savefig("build/plot-t-T.pdf")