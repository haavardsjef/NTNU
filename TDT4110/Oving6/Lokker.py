# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 20:40:31 2017

@author: Haavard
"""

number_list = []
sum = 0

for i in range(100):
        number_list.append(i)
print(number_list)

for i in number_list:
    if i % 3 == 0 or i % 10 == 0:
        sum += i
print("Summen er:",sum)

for i in range(len(number_list)):
    if i % 2 == 0:
        temp = number_list[i+1]
        number_list[i+1] = number_list[i]
        number_list[i] = temp
print("Den nye listen blir: ", number_list)

for i in range(len(number_list)//2):
    temp = number_list[i]
    number_list[i] = number_list[-i-1]
    number_list[-i-1] = temp
print("Den reversete listen blir:", number_list)