import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat
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
        ydata[i] = float(values[0])
        xdata[i] = float(values[1])
        
        i+=1

xdata = 1/xdata
ydata =np.log(ydata)
x_line = np.linspace(1/270, 1/330)
plt.plot(xdata, ydata, 'bx', label="Wertepaare")
popt1, pcov1 = curve_fit(func, xdata, ydata)
plt.plot(x_line, func(x_line, *popt1), "r-", label="Ausgleichsgerade")
plt.xlabel(r"$\frac{1}{T}$ / $\frac{1}{\symup{K}}")
plt.ylabel(r"$\ln (p)$")

print(popt1)
errors = np.sqrt(np.diag(pcov1))
print(errors)
plt.legend()
plt.tight_layout()
plt.savefig("build/plot-L.pdf")
x = ufloat( 2408.07451854 , 29.66240906)
r = 8.3144598
print(x * r)
print(x*r/120.91)