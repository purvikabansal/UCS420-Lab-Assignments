#WAP to create a list of 100 random numbers between 100 and 900.

import random
count=0
randomlist=[]
for i in range(100):
    randomlist.append(random.randint(100,900))
  
 #i. All odd numbers
count_a=0
oddnum = []
for j in randomlist:
    if j % 2 != 0:
        oddnum.append(j)
        count_a++
print(f"Odd numbers: {oddnum}")
print("the count:",count_a)

#ii. All even numbers
count_even=0
evennum = []
for j in randomlist:
    if j % 2 == 0:
        evennum.append(j)
        count_even++
print(f"even numbers: {evennum}")
print("the count:",count_even)


#iii. All prime numbers
count_prime = 0
primenum= []
for i in oddnumbers: 
    if i > 1:  
        for j in range(2, i):  
            if i % j == 0:  
                break
        else:  
            primenum.append(i)
            count_prime++
print(f"Prime numbers: {primenum}")
print("The count:", count_prime)
