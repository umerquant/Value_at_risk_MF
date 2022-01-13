import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
np.set_printoptions(precision=4, suppress= True)

sp_returns = np.loadtxt("ngen_axis_scmf.csv", delimiter = ",", usecols = 1)
sp_returns.mean()
sp_returns.std()

x = np.linspace(-15.0, 10.0, 1000)
y = stats.norm.pdf(x, loc = sp_returns.mean(), scale = sp_returns.std())

plt.figure(figsize = (20, 8))
plt.hist(sp_returns, density = True, bins = 200, label = "Axis Small Cap (NGEN Data) daily returns 2016-2022")
plt.plot(x, y, label = "Normal Distribution")
plt.title("Normality of Axis Small Cap (NGEN Data)", fontsize = 20)
plt.xlabel("daily returns",  fontsize = 15)
plt.legend(fontsize = 15)
plt.show()