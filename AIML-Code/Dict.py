#dict

#syntax:{key:value}
#heter
#ordered
#index(not numeric)
#key duplicate allowed but old gets overwritten
#Value Dublicate allowed
#data mutable(value only)


data={"name":"Let us c","Author":"Y Kanetker","price":340,"publication":"BPB Publication"}

print("Data type :",type(data))
print("Length of Data : ",len(data))

print(data)

print(data["Author"])

data["price"]=400
print(data)


