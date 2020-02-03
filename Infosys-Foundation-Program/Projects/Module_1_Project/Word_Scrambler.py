
import random

def scramble(s,word):
    s = list(s)
    random.shuffle(s)
    s = ''.join(s)
    word = word.replace(word[1:-1],s)
    return word

file = input("Enter file name : ")
with open(file,'r') as inFile:
    content = inFile.readlines()

scrambled_words = list()

for line in content:
    result = list()
    words = line.split()
    for word in words:
        if len(word) > 3:
            if word[-1:] in ('.',',',';','?','!'):
                if len(word[:-1]) > 3:
                    p = word[-1:]
                    scrble = word[1:-2]
                    word= scramble(scrble,word[:-1]) + p
                    result.append(word)
                else:
                    result.append(word)
            else :
                scrble = word[1:-1]
                word = scramble(scrble,word)
                result.append(word)
        else:
            result.append(word)
    scrambled_words.append(result)

file = file.split('.')[0] + 'Scrambled.' + file.split('.')[1]    
with open(file,'w') as outFile:
    for line in scrambled_words:
        line = ' '.join(line)
        outFile.write(line)
        outFile.write('\n')


    
