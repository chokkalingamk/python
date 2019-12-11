print ("Example for simple if")
print ("----------------------")

x=int(input("Enter the value for x"))
y=int(input("Enter the value for x"))
z=int(input("Enter the value for x"))
a=int(input("Enter the value for x"))

if x>y:
    if x>z:
        if x>a:
            print("X is the greates among all the numbers")
        else:
            print("x is not greater of a")
    else:
        print("x is not greate than z")
else:
    print("x is not greater than y")
