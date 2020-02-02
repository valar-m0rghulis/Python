

inFile = open('TestFile1.txt','r')
content = inFile.read()
inFile.close()
print("File1 Content : ")
print(content)

line = content.replace('"','/"')

outFile = open('TestFile2.txt','w+')
outFile.write(line)
outFile.seek(0)
content = outFile.read()
outFile.close()
print("File2 Content : ")
print(content)

'''
OUTPUT :

File1 Content : 
Jack said, "Hello Pune".
File2 Content : 
Jack said, /"Hello Pune/".

'''
