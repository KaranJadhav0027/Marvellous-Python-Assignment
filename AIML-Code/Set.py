#set Info

#syntax:{}
#heter
#unordered
#unindexed
#duplicate not allowed
#set is Mutable
#data is immutable

data={10,90.67,"Hello",True,10}
print("Datatype is :",type(data))
print("Length is :",len(data))
print(data)

data.add(71)
print(data)

data.remove(10)
print(data)

print("Data using Loop")
for value in data:
    print(value)
#print(data[0])
