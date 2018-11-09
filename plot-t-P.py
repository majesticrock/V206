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

werte = csv_read("csv/zeit-leistung.csv")
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
        errX[i] = float(values[1]) #* xdata[i]
        errY[i] = float(values[3]) # * ydata[i]
        i+=1

x_line = np.linspace(0, 1080)
plt.errorbar(xdata, ydata,  xerr = errX, yerr=errY, fmt = ".", label="Messwerte")
popt1, pcov1 = curve_fit(func, xdata, ydata)
plt.plot(x_line, func(x_line, *popt1), "r-", label="Fit")

plt.xlabel(r"$t$ / s")
plt.ylabel(r"$P$ / W")

print(popt1)

plt.legend()
plt.tight_layout()
plt.savefig("build/plot-t-P.pdf")
#x = np.linspace(0, 2 * np.pi, 10)
#errX = 0.4 * np.random.randn(10)
#errY = 0.4 * np.random.randn(10)

#plt.errorbar(x + errX, x + errY, xerr=0.4, yerr=errY, fmt='o')
