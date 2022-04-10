import numpy as np
import math
####################################################
# Function 1
# gives us cos value
in_array = [0, math.pi / 2, np.pi / 3, np.pi]
print("Input array : \n", in_array)

cos_Values = np.cos(in_array)
print("\nCosine values : \n", cos_Values)
####################################################
# Function 2
# gives us sin value
in_array = [0, math.pi / 2, np.pi / 3, np.pi]
print("Input array : \n", in_array)

sin_Values = np.sin(in_array)
print("\nCosine values : \n", sin_Values)
####################################################
# Function 3
# helps us changing number at specific location
u = np.ones((10,10))
u[1:-1,1:-1] = 3
print(u)
####################################################
# Function 4
# help us about choosing diagonal numbers
p = np.diag(4+np.arange(8))
print(p)
####################################################
# Function 5
a = np.array([18, 22, 46, 58])
b = np.arange(4)
print(10*np.sin(a))
####################################################
# Function 6
# helps us with elimination operations with boolean
a = np.array([18, 22, 46, 58])
b = np.arange(4)
print(a < 23)
####################################################
# Function 7
# helps us log operations
x = [2, 4, 6, 10]
print("x        =", x)
print("ln(x)    =", np.log(x))
print("log2(x)  =", np.log2(x))
print("log10(x) =", np.log10(x))
####################################################
# Function 8
# gives us sum of all elements
x = np.random.random((3,4))
print(x)
print(x.sum())
####################################################
# Function 9
# gives us minimum number
y = np.random.random((4,5))
print(y)
print(y.min())
####################################################
# Function 10
# give us maximum number
z = np.random.random((4, 5))
print(z)
print(z.max())
####################################################
# Function 11
# for absolute value calculation
x = np.array([-32, -75, 0, 78, 2])
absolute = abs(x)
print(absolute)
####################################################
# Function 12
# for exponential operations
q = [2, 4, 6]
print("q     =", q)
print("2^q   =", np.exp2(q))
print("3^q   =", np.power(3, q))
####################################################