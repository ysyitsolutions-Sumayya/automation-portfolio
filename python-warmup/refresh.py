
person = {"Name": "Ali", "Address" : {"city":"Dubai"}}

print(person["Address"]["city"])
print(person.get("phone", "unknown"))
print(person.get("Name"))

people = [{"name":"Yunus", "Address": {"city": "Al Ain"}}, 
          {"name":"Yahya", "address": {"city":"Abu Dhabi"}} , 
          {"name":"Sumayya" , "Addresss": {"city": "Dubai"}}]
names = [person["name"] for person in people]
print(names)

def greeting(name="friend"):
    return f"hello, {name}!"

print(greeting())
print (greeting("yusuf"))

try :
    print(person["phone"])
except KeyError:
    print("Key does not exist")

with open("example.txt","w", encoding="utf-8") as file:
       file.write("This line was written using with open().\n")