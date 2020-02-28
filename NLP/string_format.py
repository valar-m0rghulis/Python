name = "Deepak"
print(f"My name is {name}")

d = {'a':123, 'b':456}
l = [0,1,2]

print(f"My number is {d['a']}")

print(f"My number is {l[1]}")

lib = [('pillow','keras','pafy','spaCy'),('Image','NN','Video','NLP')]

print(lib)

for a,b,c,d in lib:
    print(f"{a:10} {b:10} {c:10} {d:10}")
    