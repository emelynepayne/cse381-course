'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

mn = 0
mx = len(primes)

target = 100

for i in range(10):
guess = int((mn+mx)/2)

if primes[guess] == target:
print ("target found in index number : "+ str(primes.index(primes[guess])))
break

elif mx == 0 or mn == len(primes)-1 or mx == mn + 1:
print ("number not found")
break
elif primes[guess] > target:
mx = guess
elif primes[guess] < target:
mn = guess