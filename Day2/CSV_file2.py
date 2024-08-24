import csv

Employee=[
    ["name","mobile","Block","salary"],
    ["praveen","99393939","data science",55000],
    ["samad","7892496","data science",89000]
]

with open("Employee.csv",mode="w",newline='') as data:
    file=csv.writer(data)
    file.writerows(Employee)