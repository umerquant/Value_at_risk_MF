#Historical VAR 
#Author - Umer

import numpy as np
import matplotlib.pyplot as plt

sp_returns = np.loadtxt("ngen_axis_scmf.csv", delimiter = ",", usecols = 1)
sp_returns.size

I0 = 100000            #Investment position in the particular Asset /Index. 
prob = 0.35

np.percentile(sp_returns, prob * 100)

var_h = np.percentile(sp_returns, prob * 100) * I0 #Historical Value at Risk 

print(var_h)

