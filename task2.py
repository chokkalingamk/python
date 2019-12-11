print("Program is to check the Student examination")
print(" Enter the Name of the name of the Student")
name = input()
print(" Enter the Age of the Student")
age = int(input())
print("Enter the Mark of Science")
science=float(input())
print("Enter the Mark of Maths")
maths=float(input())
print("Enter the Mark of English")
eng=float(input())
print("Enter the Mark of language")
lang=float(input())
total=(science+maths+eng+lang)
avg=total/4
if(avg > 40):
    if(avg > 60):
        if(avg>70):
            if(avg>=80):
                print(name,"Achieved firstclass with Designation")
            else:
                print(name,"Achived first class")
        else:
            print(name,"Achived Second class")
    else:
        print(name,"Achieved thrid class")
else:
    print(name,"Didnt pass the examination")
