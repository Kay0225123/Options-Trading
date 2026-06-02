import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import math

# Generating random array of values between 50 - 150
#S is the stock price
S = np.linspace(50, 150, 20)
# strike price
K = float(input("Enter the strike price: "))
#Cumulative distribution function
#N()
#Time left til maturity (in years)
T = float(input("Enter the time left till maturity(in years): "))
#risk free rate
r = float(input("Enter the trisk free rate: "))
#Volatility
sigma = float(input("Enter the volatility: "))

#Calculating D1 and D2 
d1 = (np.log(S/K) + (r + (sigma**2)/2)*T) / (sigma*np.sqrt(T))
d2 = d1 - sigma*np.sqrt(T)

#Calculating Calls and Puts
Call = S * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)
Put = K * np.exp(-r*T) * norm.cdf(-d2) - S * norm.cdf(-d1)

## I am gonna need two axes inside my figures
fig, (ax1, ax2) = plt.subplots(ncols=2) 

ax1.scatter(S, Call)
ax2.scatter(S, Put)

ax1.set_title('Call')
ax2.set_title('Put')
plt.show()
