"""
Write a program that includes information about the grades of 5 students
in a school.
- Keep these students' grades in a list. (Midterm, final, homework)
- Keep students' names in a list. (Name, surname)
- Create a dictionary named info and put all the information of students in
a dictionary.
- Sort and list the students' grades here in descending order and
congratulate the student with the highest score.

"""

students = []
grades = []
info = {}

for i in range(5):
    studentName = input("Enter Your Name : ")
    students.append(studentName)
    studentSName = input("Enter Your Surname : ")
    students.append(studentSName)
    
#--- Control Flag ---#
    midtermFlag = True
    finalFlag = True
    homeworkFlag = True
#--------------------#

    while True:

        if (midtermFlag == True):
            midterm = int(input("Enter Your Midterm Grade :"))
            if ( midterm > 0 and midterm <= 100):
                grades.append(midterm)
                midtermFlag = False
            else:
                print("You have entered an invalid value. Please enter a value between 1 and 100")
                continue
            
            

        if (finalFlag == True):    
            final = int(input("Enter Your Final Grade :"))
            if ( final > 0 and final <= 100):
                grades.append(final)
                finalFlag = False
            else:
                print("You have entered an invalid value. Please enter a value between 1 and 100")
                continue
            

        if(homeworkFlag == True):
            homework = int(input("Enter Your homework Grade :"))
            if ( homework > 0 and homework <= 100):
                grades.append(homework)
                homeworkFlag = False
            else:
                print("You have entered an invalid value. Please enter a value between 1 and 100")
                continue
            

        if (not midtermFlag and not finalFlag and not homeworkFlag):
            break
    
    
    average = (midterm+final+homework)/3

    info[students[2*i]+" "+students[2*i+1]]=[midterm,final,homework,average]

orderedInfo = {k: v for k, v in sorted(info.items(), key=lambda item:item[1],reverse=True )}
print("\n")

for k,v in orderedInfo.items():
    print(k,v)
    
for k in orderedInfo:
    print(f"{k} received the highest grade. Congratulations! ")
    break
