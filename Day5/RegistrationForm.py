import tkinter as tk

# configuration
window=tk.Tk()
window.title("student registration")
window.state("zoomed")


#font family
fontfamily='Arial'
h1=(fontfamily,25,"bold")
h2=(fontfamily,22,"bold")
h3=(fontfamily,20,"bold")
h4=(fontfamily,18,"bold")
h5=(fontfamily,15,"bold")
lbl=(fontfamily,12,"bold")
para=(fontfamily,12,"bold","italic","underline")

## body ##
div1=tk.Frame(window,bg="#f0f",height=50)
div1.pack(fill=tk.X, anchor="n")


Heading=tk.Label(div1,bd=5,relief="groove",text="Student Registration",font=para,fg="#046",bg="lightblue")
Heading.pack(fill=tk.X)


## Main Body ##
div2=tk.Frame( window,bg="#0f0",bd=5,relief="ridge",height=40)
div2.pack(fill=tk.X)

## form frame

form=tk.Frame(div2,bg="#f00",bd=10,height=100,width=200)
form.pack(pady=50)
