from scipy.stats import entropy
from math import log

print("Dado Justo:", entropy([1/6,1/6,1/6,1/6,1/6,1/6], base=2)) #forma 1
print("Dado Justo:", -((1/6)*log(1/6, 2)+(1/6)*log(1/6 ,2)+(1/6)*log(1/6 ,2)+
                       (1/6)*log(1/6 ,2)+(1/6)*log(1/6 ,2)+(1/6)*log(1/6,2))) #forma 2

print("Dado Injusto:", entropy([1/3,1/3,1/12,1/12,1/12,1/12], base=2))
print("Dado Injusto:", -((1/3)*log(1/3, 2)+(1/3)*log(1/3 ,2)+(1/12)*log(1/12 ,2)+
                       (1/12)*log(1/12 ,2)+(1/12)*log(1/12 ,2)+(1/12)*log(1/12,2)))