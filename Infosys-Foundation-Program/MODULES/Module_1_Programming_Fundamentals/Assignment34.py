

with open('rhyme.txt','r') as inFile:
    content = inFile.readlines()
    
print("File Content : \n\n")

word_count = dict()

for line in content:
    line = line.strip().lower()
    print(line)
    words = line.split()
    for word in words:
        count = 0
        if word in word_count:
            count+=1
            word_count[word]= word_count[word]+count
        else:
            count+=1
            word_count[word]=count
            

print("\n\nWord Count:\n\n")    
with open('words.txt','w+') as outFile:
    for i,v in word_count.items():
        outFile.write(i+"    "+str(v)+"\n")
with open('words.txt','r')as result:        
    content = result.read()

print(content)


'''
OUTPUT :

File Content : 


jingle bells jingle bells
jingle all the way
what fun it is to ride
in a one horse open sleigh
jingle bells jingle bells
jingle all the way


Word Count:


jingle    6
bells    4
all    2
the    2
way    2
what    1
fun    1
it    1
is    1
to    1
ride    1
in    1
a    1
one    1
horse    1
open    1
sleigh    1

'''

