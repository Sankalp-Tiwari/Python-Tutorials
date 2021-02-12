'''
Author : Sankalp
Date : 23 January 2021
Purpose : Practise Problem
'''


def next_palindrome(n):
    if n>10:
        n = n + 1
        while not is_palindrome(n):
            n += 1
        return n
    if n<10:
        return n
    if n==10:
        n = n + 1
        while not is_palindrome(n):
            n += 1
        return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == '__main__':
    n = int(input("Enter the numbers of test cases\n"))
    numbers = []
    for i in range(n):
        number = int(input("Enter the number\n"))
        numbers.append(number)
    for item in numbers:
        print(next_palindrome(item))