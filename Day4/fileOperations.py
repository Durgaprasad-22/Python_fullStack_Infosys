# with open("sampleFile.txt" mode="x",newline='') as file
# another format

try:
    file=open("sampleFile.txt" , "x")
    file.write("hello world")
    file.close()
except FileExistsError as e:
    print(" file is already is there..!")
    key=input(" do you want to replace it ? (yes/no)\n ")
    if key.strip().lower()=="yes":
        file=open("sampleFile.txt" , "w")
        file.write(" hello world")
        file.close()
    elif:
        print(" file not replaced")    
    else:
        print(" enter correct command")

finally:
    print(" process completed")
