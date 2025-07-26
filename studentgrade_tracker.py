 # Q1 - STUDENT GRADE TRACKER    #

subject = []
marks = []

sub_1 = input("Enter The Subject 1 : ")
sub_2 = input("Enter The Subject 2 : ")
sub_3 = input("Enter The Subject 3 : ")
subject.append(sub_1)
subject.append(sub_2)
subject.append(sub_3)

mark_1 = int(input(f"Enter the marks of {sub_1} :"))
mark_2 = int(input(f"Enter the marks of {sub_2} :"))
mark_3 = int(input(f"Enter the marks of {sub_3} :"))
marks.append(mark_1)
marks.append(mark_2)
marks.append(mark_3)
print("Subjects you input :" , tuple(subject))
print("The marks you input for corresponding subjects : ", tuple(marks))
print("The total marks obtained : " ,mark_1+mark_2+mark_3)
print("The Average Of marks is : " ,(mark_1+mark_2+mark_3) // 3 )

