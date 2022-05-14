# Write a Python program to count the number of even and odd numbers from a series of numbers.

a = (1,2,3,4,5,6,7,8,9)
b = len(a)
even_count = odd_count = 0

for i in range(0,b,1):
    if a[i]%2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
    
print("Number of even numbers :",even_count)
print("Number of odd numbers :",odd_count)