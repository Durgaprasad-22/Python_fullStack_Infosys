import csv

with open("student.csv", mode="r") as data:
    students=csv.reader(data)
    n=0
    for student in students:
        if n==0:
            if student[0].lower() != "name":
                print("first column must be Name")
                break
            elif student[1].lower() != "marks":
                print("sencond column should be marks")
                break
        else:
            print(" - ".join(student))
        
        n=n+1

                
        
