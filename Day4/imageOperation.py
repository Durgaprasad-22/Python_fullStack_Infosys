from PIL import Image

file=open("anaconda.png","rb")

img= Image.open(file)

img.show()