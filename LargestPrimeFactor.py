'''

Online Python Compiler.
Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def isNumberPrime(number):
    i = 2
    while i < number // 2:
        if number % i == 0:
            return False 
        i = i + 1
    return True


num = 600851475143
primeNumber = 2

while isNumberPrime(num) == False:
    while num % primeNumber != 0:
        primeNumber = primeNumber + 1
        while isNumberPrime(primeNumber) == False:
            primeNumber = primeNumber + 1

    if num % primeNumber == 0:
        num = num/primeNumber 
        
print(num)