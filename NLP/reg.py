text = "The phone number of the agent is 991-991-7860. Call soon!"
print("991-991-7860" in text)

import re
pattern = "phone"
print(re.search(pattern,text))
match = re.search(pattern,text)
print(match.span())
print(match.start())
print(match.end())

text = 'my phone is new phone'
match = re.search(pattern,text)
print(match.span())
print(re.findall("phone",text))

text = "The phone number of the agent is 991-991-0000. Call soon!"
pattern = r'\d\d\d-\d\d\d-\d\d\d\d'
number = re.search(pattern,text)
print(number.group())

pattern = r'\d{3}-\d{3}-\d{4}'
number = re.search(pattern,text)
print(number.group())

print(re.findall(r"[^\d]+",text))
