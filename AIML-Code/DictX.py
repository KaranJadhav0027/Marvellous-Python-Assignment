
data={"name":"Let us c","Author":"Y Kanetker","price":340,"publication":"BPB Publication"}

print("loop to disply Keys")
for value in data:
    print(value)

print("loop to disply Values")
for x in data.values():
    print(x)

print("loop to display Key and Values")
for X,Y in data.items():
    print(X,Y)
