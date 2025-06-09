#List Info

#syntax: []
#heterogenious
#order
#index
#data mutable
#list mutable
#duplicate allowed

data=[10,19.67,"Hello",40,True]

print("datatype is :",type(data))
print("length is :",len(data))
print(data)

print(data[0])
print(data[1])
print(data[2])
print(data[3])

data[0]=11
print(data[0])

data.append(40)
print(data[4]) 

print("Data Display  using loop")

for Value in data:
    print(Value)
