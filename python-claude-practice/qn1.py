#qn1
user = {"name": "Ali", "contact":{"email":"ali.2026@gmail.com"}}

print(user["contact"]["email"])
print(user.get("phone-number", "not provided"))
user["active"] = True
value_pop= user.pop("contact")
print(value_pop)
print(user)