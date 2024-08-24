import csv

data=[
    ["s.no","roll","name","mobile","email"],
    ["1","201","durga","  99494949","durga@gmail.com"],
    ["2","","pravenn","9826589",""],
    ["3","201","samad","99494949","samad@gmail.com"],
    ["4",202,"stanley","9826589","stanley@gmail.com"]
]
# print(data[1])
# print(data[0])

def validate(record):
    roll=str(record[1])
    if len(roll) !=3 or not roll.isnumeric():
         return False
         
    name=record[2].replace(" ","")
    if not name.isalpha():
         return False
    
    
    
    mobile=record[3].strip()
    if not mobile.isnumeric():
         return False
    
    email=record[4].strip()
    if len(email)==0 or email=="" or "@" not in email:
         return False
    
    data=[record[1],record[2],record[3],record[4]]
    return data


finalData=list(filter(validate,data[1:]))
print(finalData)

try:
    with open("sample.csv",mode="r") as file:
       pass
except:
    print("file does't exits")
    print("creating new file..")

with open("sample.csv", mode="w",newline='') as file:
         file1=csv.writer(file)
         file1.writerow(data[0])
         i=1
         for record in finalData:
              record[0]=i
              file1.writerow(record)
              i=i+1
    
with open("sample.csv","r") as file:
         out=csv.reader(file)
         print(out)
    
       
               
                

# import csv

# data = [
#     ["s.no", "roll", "name", "mobile", "email"],
#     ["1", "201", "durga", "99494949", "durga@gmail.com"],
#     ["2", "", "pravenn", "9826589", ""],
#     ["3", "201", "samad", "99494949", "samad@gmail.com"],
#     ["4", "202", "stanley", "9826589", "stanley@gmail.com"]
# ]

# def validate(record):
#     if len(record) < 5:
#         return None

#     roll = record[1].strip()
#     if not roll.isdigit() or len(roll) == 0:  # Roll number should be numeric and non-empty
#         return None

#     name = record[2].strip()
#     if not name.isalpha():  # Name should be alphabetic
#         return None

#     email = record[4].strip()  # Email is in the correct position
#     if "@" not in email or "." not in email:  # Basic email validation
#         return None

#     mobile = record[3].strip()
#     if not mobile.isdigit() or len(mobile) < 10:  # Mobile number should be numeric and at least 10 digits
#         return None

#     return [record[1], record[2], record[3], record[4]]

# # Validate the data excluding the header
# validated_data = list(filter(None, map(validate, data[1:])))
# print("Validated Data:", validated_data)

# # Try to read from file
# try:
#     with open("sample.csv", mode="r") as file:
#         print("File exists, reading data...")
#         file_data = list(csv.reader(file))
#         print(file_data)
# except FileNotFoundError:
#     print("File does not exist. Creating new file...")

# # Write validated data to file
# with open("sample.csv", mode="w", newline='') as file:
#     file_writer = csv.writer(file)
#     file_writer.writerow(data[0])  # Write the header
#     file_writer.writerows(validated_data)  # Write validated data

# # Read and print the file content to verify
# with open("sample.csv", mode="r") as file:
#     out = list(csv.reader(file))
#     print("File Content:")
#     print(out)


