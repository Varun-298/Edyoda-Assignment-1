# Write a Python program that accepts a word from the user and reverse it.

name = input('Enter a name which you needs to be printed in mirror dimension : ')
a = list(name)
b = len(name)-1

for i in range(b,-1,-1):
    print(a[i],end="")


