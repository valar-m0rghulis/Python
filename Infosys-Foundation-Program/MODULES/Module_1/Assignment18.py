
# Python program to count number of alphabet in string.

s = input("Enter string : ")

print(s)

s = s.lower()
char = list()
for i in s:
    if i not in char:
        print(s.count(i),i)
        char.append(i)

'''
OUTPUT :

Enter string : ABcdaBadCb
ABcdaBadCb
3 a
3 b
2 c
2 d

'''
