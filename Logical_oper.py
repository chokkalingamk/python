#This is the Bitwise program to check
print ("Welcome to Addition Calculator")
print ("Enter the value A")
a = int(input())
print ("Enter the value B")
b = int(input())
print ("Enter the value C")
c = int(input())
if ( a > b and a > c ):
    print ("Value of A is greater: ", a)
elif (b > a and b > c):
    print ("Value of B is greater:", b)
else:
    print ("value of C is greater:", c)

