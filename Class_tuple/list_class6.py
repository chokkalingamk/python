print("List Manipulations")
print("------------------")

x=[100,"BSS",99.9,89+9j,True,"python","vani","chokka","Jaya","Aditi"]
print ("value of x is:",x)
flag=False
i=0
l=len(x)
while i<=l:
    if x[i]=="chokka":
        print ("found")
        flag=True
    i=i+1
if flag==1:
    print("found")
else:
    print("not found")

if "Aditi" in x:
    print("Found")
else:
    print("not found")