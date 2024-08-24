import tkinter  as tk

root=tk.Tk()

def get_btn1():
    input_data=textbox.get()
    label1.config(text=input_data)

def get_btn2():
    input_data=textbox.get()
    label2.config(text=input_data)
    

root.title("hello")

root.geometry("600x400")


label1=tk.Label(root,text="first label")
label1.pack(pady=10)

label2=tk.Label(root,text="second label")
label2.pack(pady=10)

textbox=tk.Entry(root,width=50)
textbox.pack(pady=20)


btn1=tk.Button(root,text="Button -1",command=get_btn1)
btn1.pack(pady=10)

btn2=tk.Button(root,text="Button -2",command=get_btn2)
btn2.pack(pady=10)


