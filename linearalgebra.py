## Linear Algebra
# How system of linear equation can be solved in numpy

import numpy as np

# Resources or Co-efficient of variables 

x = np.array([[2, 3, -2], 
            [1, 3, -3], 
            [3, -6, 1]])

# Total units provided 

y = np.array([4, 4, -3])

# Solving 
a = np.linalg.solve(x,y)

print("Solution: ", a)