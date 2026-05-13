# Linear regression method in Python
# Fitting y = a + bx to given n data points

import numpy as np

# Reading value of n
n = int(input("How many data points? "))

# Creating numpy arrays x & y to store n data points
x = np.zeros(n)
y = np.zeros(n)

# Reading data
print("Enter data:")

for i in range(n):
x[i] = float(input("x[" + str(i) + "] = "))
y[i] = float(input("y[" + str(i) + "] = "))

# Finding required sums for least square method
sumX, sumX2, sumY, sumXY = 0, 0, 0, 0

for i in range(n):
sumX = sumX + x[i]
sumX2 = sumX2 + x[i] * x[i]
sumY = sumY + y[i] # corrected
sumXY = sumXY + x[i] * y[i]

# Finding coefficients a and b
b = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX * sumX)
a = (sumY - b * sumX) / n

# Displaying coefficients a, b & equation
print("\nCoefficients are:")
print("a:", a)
print("b:", b)

print("And equation is: y = %0.4f + %0.4f x" % (a, b))

output:
How many data points? 3
Enter data:
x[0] = 1
y[0] = 2
x[1] = 2
y[1] = 3
x[2] = 3
y[2] = 5

Coefficients are:
a: 0.3333333333333333
b: 1.5
And equation is: y = 0.3333 + 1.5000 x