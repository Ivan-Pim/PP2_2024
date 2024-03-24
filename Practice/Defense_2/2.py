import json

file = open("data.JSON")

data = json.load(file)

print(f"{"id":<5}{"name" :<15}{"age" :<5}{"city" :<20}{"email" :<40}")
for i in data:
    for x in i:
        print(x + ":", i[x])
    print("\n")

print('-'*50)

for i in data:
    print(i["name"] + "   ", i["email"])