
data=[
    ["tester","1234","tester@gmail.com"],
    ["sample","56678","sample@gmail.com"]
    ]

with open("sample.txt","w") as file:
    for i in data:
        x=" - ".join(i)
        file.write(x)
        file.write("\n")    

with open("sample.txt","r") as file:
    out=file.read()
    print(out.strip())