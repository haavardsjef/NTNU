import math

numb = [8,8.4,7.5,7.8,8]
n = len(numb)
Z = 1.960 # For 95% the Z value is 1,960

def mean(numb, n):
    sum = 0
    for i in range(len(numb)):
        sum += numb[i]
    return sum / n

def SD(numb, n):
    return math.sqrt(variance(numb, n))


def variance(numb, n):
    avg = mean(numb, n)
    temp = 0
    for i in range(len(numb)):
        temp += (numb[i]-avg)**2
    return temp / n


print(mean(numb, n))
print(variance(numb ,n))
print(SD(numb, n))

print()

print(mean(numb, n),"+/-", (Z*SD(numb, n))/(math.sqrt(n)))
print(mean(numb, n) + (Z*SD(numb, n))/(math.sqrt(n)))
print(mean(numb, n) - (Z*SD(numb, n))/(math.sqrt(n)))
