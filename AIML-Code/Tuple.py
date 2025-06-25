#Tuple Info

#syntax : ()
#heter
#ordered
#index
#data immutable
#Tuple Immutable
#Duplicate allowed

data=(10,"hello",90.67,True,10)

print("Data type is :",type(data))
print("Length is :",len(data))
print(data)

print(data[0])
print(data[1])

#data[0]=11

print("Data using loop")
for value in data:
    print(value)

for Value in range(len(data)):
    print(data[Value])
