import tkinter  as tk

root=tk.Tk()

root.title("hello")

root.geometry("600x400")


label1=tk.Label(root,text="WELCOME STANLEY")
label1.pack(pady=10)

textbox=tk.Entry(root,width=50)
textbox.pack(pady=20)


btn=tk.Button(root,text="Button -1")
btn.pack(pady=10)

