print("Program is to Validate the voting if the candidate age is less than 18")

print(" Enter the Name of the Candidate")
name = input()
print(" Enter the Age of the Candidate")
age = int(input())

if(age>=18):
    print(name,"is eligible for Voting")
else:
    print(name,"is less than 18 so not eligible")