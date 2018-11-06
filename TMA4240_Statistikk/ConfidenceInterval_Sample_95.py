# Calculating 95percent confidence interval for a samples
# Written by Håvard Hjelmeseth
# 06.11.2018

# Importing modules
import math

# Inital data
numb = [8,8.4,7.5,7.8,8] # EDIT THIS ARRAY TO YOUR NEEDS
n = len(numb) # This does not need to be edited


# Deciding Z - value
# Edit this part depending on if n >= 30.
# By default it works for n < 30

# Include this part if n >= 30:
# Z = 1.960 # For 95% the Z value is 1,960
# print("Using normal distribution!")

# If you included the paragraph above, then this needs to be commented out.
# This is the Z value for a t-distribution instead of a normal distribution
# Use this only when n < 30
Z = 2.776
print("Using t-distribution!")



# Define functions
def mean(numb, n):
    sum = 0
    for i in range(len(numb)):
        sum += numb[i]
    return sum / n

def SD(numb, n):
    return math.sqrt(SampleVariance(numb, n))


def SampleVariance(numb, n):
    avg = mean(numb, n)
    temp = 0
    for i in range(len(numb)):
        temp += (numb[i]-avg)**2
    return temp / (n-1)


# Call functions
print("Sample mean:", mean(numb, n))
print("Sample variance:", SampleVariance(numb ,n))
print("Sample standard deviation:", SD(numb, n))

print()

print("We can be 95% sure that mu equals:", mean(numb, n),"+/-", (Z*SD(numb, n))/(math.sqrt(n)))
print("Upper bounds:", mean(numb, n) + (Z*SD(numb, n))/(math.sqrt(n)))
print("Lower bounds:", mean(numb, n) - (Z*SD(numb, n))/(math.sqrt(n)))

input()
