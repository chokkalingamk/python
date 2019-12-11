print("List Manipulations")
print("------------------")

x=[100,"BSS",99.9,89+9j,True,"python","Jaya","Aditi"]
print ("value of x is:",x)

x.append("newpython")
print("After appending the single value",x)

y=[100,200,300,400,500]
x.append(y)
print("after append the list",x)
print (x[9])
print (x[9][2])

z=[1,2,3,4,5]
x.extend(z)
print("AFter extending z and x :",x)

x.insert(2,"modpython")
print("After inserting x",x)

z1=[12,13,14]
x.insert(3,z1)
print("After inserting x in z",x)