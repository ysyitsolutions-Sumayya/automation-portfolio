#qn 3
text = "hello world hello hi how are you hello"
if text.strip() == "":
     print("No string provided")
     exit()

text_dict = {}
n = text.lower()

text_words = n.split()
for word in text_words:
        if word in text_dict:
            text_dict[word] += 1
        else:
            text_dict[word] = 1

print(text_dict)

#version2
from collections import Counter
print("Version 2")
text2 = "The car and the cycle and the bus are all vehicles."
counts = Counter(text2.lower().split())
print(counts)