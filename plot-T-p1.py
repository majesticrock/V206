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

werte = csv_read("csv/temperatur-druck1.csv")
xdata = np.zeros(18)
ydata = np.zeros(18)
errX = np.zeros(18)
errY = np.zeros(18)

ignore = True
i=0
for values in werte:
    if(ignore):
        ignore = False
    else:
        xdata[i] = float(values[0])
        ydata[i] = float(values[2])
        errX[i] = float(values[1])
        errY[i] = float(values[3])
        i+=1

x_line = np.linspace(297.7, 323.6)
plt.errorbar(xdata, ydata, xerr = errX, yerr= errY, fmt = ".", label="Messwerte")
popt, pcov = curve_fit(func, xdata, ydata)
plt.plot(x_line, func(x_line, *popt), "r-", label="Fit")

plt.xlabel(r"$T_1$ / K")
plt.ylabel(r"$p_b$ / $10^5$pa")

plt.legend()
plt.tight_layout()
plt.savefig("build/plot-T-p1.pdf")