import tkinter  as tk

root=tk.Tk()

def get_btn():
    input_data=textbox.get()
    label1.config(text=input_data)

root.title("hello")

root.geometry("600x400")


label1=tk.Label(root,text="WELCOME STANLEY")
label1.pack(pady=10)

textbox=tk.Entry(root,width=50)
textbox.pack(pady=20)


btn=tk.Button(root,text="Button -1",command=get_btn)
btn.pack(pady=10)

