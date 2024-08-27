# with open("sampleFile.txt" mode="x",newline='') as file
# another format

try:
    file=open("sampleFile.txt" , "x")
    file.write("hello world")
    file.close()
except FileExistsError as e:
    print(" file is already is there..!")
finally:
    print(" process completed")
