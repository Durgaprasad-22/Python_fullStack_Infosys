try:
    def Fileoperation(filename,mode):
        with open(f"{filename}.txt",mode) as file:
            while True:
                data=input("enter some data: ")
                if data.strip().lower() == "no":
                    print("terminating...")
                    break
                else:
                    file.write(str(data)+"\n")
except FileExistsingError as e:
    print(f"File already exits with this name")
    yesOrNo= input(("do you want to relace it ? (yes / no)")).strip().lower()
    if yesOrNo == "yes":
        fileoperation("sample","w")
    else:
        exit()

Fileoperation("sample","a")   

    

    
    