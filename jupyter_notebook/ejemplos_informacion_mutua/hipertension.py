import numpy as np
from math import log
from sklearn.feature_selection import mutual_info_classif

#vejez -----> 0 : No     1 : Si
#sobrepeso -> 0 : No     1 : Si

#[vejez, sobrepeso]

X = np.array([[0, 0],
              [1, 0],
              [1, 1],
              [1, 1],
              [1, 0],
              [1,  1],
              [1, 0]])

#hipertensión ---> 0 : No   1 : Si
Y= np.array([0, 0, 1, 1, 0, 1, 0])

print("Información mutua:", mutual_info_classif(X,Y, discrete_features=True))