# Write a Python program that accepts a word from the user and reverse it.

name = input('Please Enter a name : ')
a = list(name)
b = len(name)-1
print("The mirror dimension of your enterned name is as below:")

for i in range(b,-1,-1):
    print(a[i],end="")


