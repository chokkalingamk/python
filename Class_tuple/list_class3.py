print("List Manipulations")
print("------------------")

x=[100,"BSS",99.9,89+9j,True]
print ("value of x is:",x)

print("using While loop")
print("-----------------------")

i=0
l=len(x)
print("total number of elements are :",l)
while i<l:
    print (x[i])
    i=i+1

print("Using For loop")
print("--------------")
for i in x:
    print(i)