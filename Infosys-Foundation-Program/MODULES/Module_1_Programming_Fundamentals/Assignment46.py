

import re
student_id = input("Enter Student Id:")
if(re.search(r"[a-z|A-Z]",student_id)):
    print("Invalid Student ID")
else:
    student_name = input("Enter Student Name:")
    if(re.search(r"[0-9]",student_name)):
        print("Invalid Name Entered")
    else:
        fees_amount = input("Enter Fees Amount:")
        dots = re.findall(r"\.",fees_amount)
        if(len(dots) > 1):
            print("Invalid Fees Amount")
        else:
            if(len(dots) == 1 and re.search(r"\.[0-9]{3}",fees_amount)):
                print("Invalid Fees Amount")
            else:
                email_id = student_name+"@"+"ABC.com"
                print("Studnet ID:",student_id)
                print("Student Name:",student_name)
                print("Fees Amount:",fees_amount)
                print("Email ID:",email_id)


'''
OUTPUT :

Enter Student Id:a123
Invalid Student ID

Enter Student Id:123
Enter Student Name:d33p
Invalid Name Entered

Enter Student Id:123
Enter Student Name:deep
Enter Fees Amount:123.123
Invalid Fees Amount

Enter Student Id:123
Enter Student Name:deep
Enter Fees Amount:123.12
Studnet ID: 123
Student Name: deep
Fees Amount: 123.12
Email ID: deep@ABC.com

'''
