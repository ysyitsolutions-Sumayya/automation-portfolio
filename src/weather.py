weather = {"city": "Dubai", "temperature": 31, "wind": 12}
print(weather["city"])

def make_report(data):
    return f"In {data['city']} it is {data['temperature']} degrees."
print(make_report(weather))