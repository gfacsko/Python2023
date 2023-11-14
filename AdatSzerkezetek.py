from typing import List, Any  # Harmadik óra

import numpy as np

#for i in range(1, 6):
#    print(i)

#s = "banana"
#for c in s:
#    print(c)

#s = "banana"
#for i in range(len(s)):
#    print(s[i])

#The not-so-python way
#s = 0
#a = [2, 3, 1, 3, 3]
#for i in range(0,len(a)):
#    s += a[i] # note this is equivalent to s = s + i
#    print(s)

#The python way
#s = 0
#a = [2, 3, 1, 3, 3]
#for i in a:
#    s += i # note this is equivalent to s = s + i
#    print(s)

# do not waste time on for cycles
#l = [2,4,6,8]
#print(np.mean(l))

#a = 133
#b = 33
#if b > a:
#    print("b is greater than a")
#elif a == b:
#    print("a and b are equal")
#elif b < a:
#    print("a is greater than b")

#numbers = []
#append two elements
#numbers.append(1)
#numbers.append(2)
#print(numbers)
#numbers.insert(0, 0)
#&print(numbers)

n=list(range(1,51))

# not so-python-way
num1 = []
for i in n:
   if i % 5 == 0:
        num1.append(i)

print(num1)

# the more python way - list comprehension
num2 = [i for i in n if i % 5 == 0]
print(num2)

