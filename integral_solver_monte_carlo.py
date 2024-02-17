#A python program that can integrate f(x) = e^x sinx 
#input the limits and number of steps
#output shows the result
#This method uses monte carlo method
#this program creates random numbers between the limits and calculates the integral
###################################################################################

import numpy as np 

a,b =  [int(x) for x in input("enter the limits of the integration\n").split()]

N = int(input("enter number of iterations\n"))
#a,b,N = 1,5,9999999  results found to be 200.59333988188507 
x= np.random.uniform(a,b, size = N) 

y = np.e**x * np.log(x)

integral = 0 
for i in range (0,N):
    integral += ((b-a)/N) * y[i] 

print(integral)

