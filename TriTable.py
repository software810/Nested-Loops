# Write a program that uses nested for loops to create the following number pyramid.

print (" Triangle of numbers ")

for i in range (1, 10): # the total number to print
    for j in range (i + 1):
        print (i * j, end = " ") #print number
# new line after each row to display pattern correctly
    print ("\n")
