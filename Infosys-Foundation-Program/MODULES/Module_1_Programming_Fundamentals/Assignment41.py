
# Dice playing.

import random

print("press Enter to start......")
key = input()
while key != "q":    
    score = random.randint(1,6)
    print(score)
    key = input()
    
'''
OUTPUT :

press Enter to start......

3

1

3

3

6

2

4

1

4

6

5

4

3
q


'''
