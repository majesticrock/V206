import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def func(x, a, b):
    return a*x +b

werte = csv_read("csv/tempbar.csv")
xdata = np.zeros(10)
ydata = np.zeros(10)
ignore = True
i=0

for values in werte:
    if(ignore):
        ignore = False
    else:
        xdata[i] = float(values[1])
        ydata[i] = float(values[0])
        i+=1
x_line = np.linspace(270, 330)
plt.plot(xdata, ydata, 'bx', label="Wertepaare")
popt1, pcov1 = curve_fit(func, xdata, ydata)
plt.plot(x_line, func(x_line, *popt1), "r-", label="Ausgleichsgerade")

plt.xlabel(r"$T$ / K")
plt.ylabel(r"$p$ / bar")

print(popt1)
plt.legend()
plt.tight_layout()
plt.savefig("build/plot-L.pdf")