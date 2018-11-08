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

ignore = True
i=0
for values in werte:
    if(ignore):
        ignore = False
    else:
        xdata[i] = float(values[0])
        ydata[i] = float(values[2])
        i+=1

x_line = np.linspace(0, 1080)
plt.plot(xdata, ydata, "r.", label="Messwerte")
popt1, pcov1 = curve_fit(func, xdata, ydata)
plt.plot(x_line, func(x_line, *popt1), "b-", label="Fit")

plt.xlabel(r"$t$ / s")
plt.ylabel(r"$P$ / W")

print(popt1)

plt.legend()
plt.tight_layout()
plt.savefig("build/plot-t-P.pdf")