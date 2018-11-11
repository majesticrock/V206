import numpy as np 
import math
import pandas as pd
from uncertainties import ufloat

CW = ufloat(12500, 500)
CK = ufloat(750, 0)
L = ufloat(313.04285, 0)
wert = ufloat(-0.0181, 0)
massed = (CW + CK) / L * wert
print(massed)