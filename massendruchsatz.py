import numpy as np 
import math
import pandas as pd
from uncertainties import ufloat

CW = ufloat(12500, 500)
CK = ufloat(750, 0)
L = ufloat(165.584, 0)
wert = ufloat(-0.021, 0.002)
massed = (CW + CK) / L * wert
print(massed)
wert = ufloat(-0.027, 0.005)
massed = (CW + CK) / L * wert
print(massed)
wert = ufloat(-0.024, 0.007)
massed = (CW + CK) / L * wert
print(massed)
wert = ufloat(-0.010, 0.010)

massed = (CW + CK) / L * wert
print(massed)

#x = np.sqrt(((12500 + 750)/313.04285)**2 * 0.002**2 + (1/313.04285 * -0.021)**2 * 500**2)
#print(x)