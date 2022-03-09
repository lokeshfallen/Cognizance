import numpy as np

print(0 * np.nan)       # any arithmetic operation on nan will result nan
print(np.nan != np.nan)  # each value of nan is differrent
print(np.inf > np.nan)  # Infinity is greater than all the values expect itself and NaN since NaN does not have fixed value
print(np.nan - np.nan)  # since the values of both the NaN will not be same and any operation on NaN will result NaN
print(0.3 == 3 * 0.1)  # Due to float precision in python 0.1 is not exactly 0.1

