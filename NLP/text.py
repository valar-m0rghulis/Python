myfile = open('sample.txt')
print(myfile)
myfile.seek(0)
content = myfile.read()
print(f"{len(content)}\n{content}")

myfile.seek(0)
lines = myfile.readlines()
print(lines)

myfile.close()

with open('test.txt', 'w+') as  myfile:
    myfile.write(content)
    print(myfile)