#Make a program that counts all the vowels in a supplied string
f = str(input())
vowels = ['a','e','i','o','u']
a = 0
for x in f:
    if x in vowels:
        a += 1
print(a)