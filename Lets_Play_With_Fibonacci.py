# Write a Python program to get the Fibonacci series between 0 to 50

a = 1 # taking variable a to store the last iteration output 
b = 0 # using variable b to store the last before iteration output
c = 1 # using variable C to print present output

print("The Fibonacci series upto 50 is as below:")
while c <= 50:
    print(c,end=" ")
    c = a + b
    b = a
    a = c
    


    
