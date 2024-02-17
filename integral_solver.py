#A python program that can integrate f(x) = e^x sinx 
#input the limits and number of steps
#output shows the result
#This method does not use monte carlo method
#this program divides the limit into equal steps and calculates the output by iterating
###################################################################################
import math
import numpy as np 

a,b =  [int(x) for x in input("enter the limits of the integration\n").split()]

N = int(input("enter number of steps\n"))

x= np.linspace(a,b,N)

y = np.e**x * np.log(x)

integral = 0 
for i in range (0,N):
    integral += ((b-a)/N) * y[i] 

print(integral)

