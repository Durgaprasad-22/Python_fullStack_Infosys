Name="Dhaneluka inst# os eng and Tech"

names=Name.split()
print(names)

for word in names:
    if not word.isalpha():
        print("Not okay")
        break


h="34 67"
j="2"
print(h.isdigit())
print(j.isnumeric())
print(h.isnumeric())
print(j.isdigit())

a=[1,2,3,4,5]
print(list(map((lambda num:num**2),a))) # using lambda function

# syntax 
# (lambda paraamter:operation),arguments)
#map(function,list or tuple)
