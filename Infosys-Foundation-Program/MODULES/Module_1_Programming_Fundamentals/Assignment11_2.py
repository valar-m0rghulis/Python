#Python prgram to calculate average of marks.

subject1 = float(input("Enter marks for subject 1 : "))
subject2 = float(input("Enter marks for subject 2 : "))
subject3 = float(input("Enter marks for subject 3 : "))

average = (subject1 + subject2 + subject3) / 3

print("Average = ", average)

subject2 += 10

average = (subject1 + subject2 + subject3) / 3

print("Average = ", average)


'''
OUTPUT :

Enter marks for subject 1 : 50
Enter marks for subject 2 : 65
Enter marks for subject 3 : 89
Average =  68.0
Average =  71.33333333333333

'''
