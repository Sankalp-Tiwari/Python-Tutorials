'''
Author : Sankalp
Date : 23 January 2021
Purpose : Practise Problem
'''
apples_having = int(input("Enter the number apples\n")) #Input of Apples
minimum = int(input("Enter the minimum number\n")) #Input of Minimum
maximum = int(input("Enter the maximum number\n")) #Input of Maximum

for i in range(minimum,maximum+1):
    if apples_having%i==0: # reminder is = 0
        print(f"{i} is divisible by {apples_having}")
    elif apples_having%i!=0: #reminder is no = 0
        print(f"{i} is not divisible by {apples_having}")

if minimum==maximum or maximum==minimum:
    print("Please select a valid range")