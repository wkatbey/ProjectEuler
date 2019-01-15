'''
LargestPrimeFactor.py
Takes an integer as input, and outputs its largest
prime factor
'''
num = int(input('Enter a number: '))

primeNumber = 2
def isNumberPrime(number):
    i = 2
    while i < number // 2:
        if number % i == 0:
            return False 
        i = i + 1
    return True

while isNumberPrime(num) == False:
    while num % primeNumber != 0:
        primeNumber = primeNumber + 1
        while isNumberPrime(primeNumber) == False:
            primeNumber = primeNumber + 1

    if num % primeNumber == 0:
        num = num//primeNumber 
        
print(num)