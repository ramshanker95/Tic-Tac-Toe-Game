from audioop import bias
import numpy as np
import matplotlib.pyplot as plt

inputs = np.array([[10,2,3], 
                   [1,0.2,0.3]])

bias = np.array([1,1,2,3])

weights = np.array([[0.1,0.2,0.3],
                    [0.1,0.2,0.3], 
                    [0.1,0.2,0.3], 
                    [0.1,0.2,0.3]])

outputs = np.dot(weights, inputs.T)
print(outputs)
print(inputs*weights.T)