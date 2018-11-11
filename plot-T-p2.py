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

werte = csv_read("csv/temperatur-druck2.csv")
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

x_line = np.linspace(273.5, 295.5)
plt.errorbar(xdata, ydata, xerr = 0.1, yerr = errY, fmt = ".", label="Messwerte")
popt, pcov = curve_fit(func, xdata, ydata)
plt.plot(x_line, func(x_line, *popt), "r-", label="Fit")

plt.xlabel(r"$T_2$ / K")
plt.ylabel(r"$p_a$ / $10^5$pa")

print(popt)

plt.legend()
plt.tight_layout()
plt.savefig("build/plot-T-p2.pdf")