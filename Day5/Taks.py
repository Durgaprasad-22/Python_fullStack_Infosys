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
div1=tk.Frame(window,bg="#f0f",height=100)
div1.pack(fill=tk.X)

leftDiv=tk.Frame(window,bg="#00f",width=300)
leftDiv.pack(fill=tk.Y,anchor="nw",side=tk.LEFT,pady=5)

rightDiv=tk.Frame(window,bg="#f00")
rightDiv.pack(fill=tk.BOTH,expand=True ,pady=5,padx=5)
