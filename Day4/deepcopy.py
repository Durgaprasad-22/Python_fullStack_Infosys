import copy

"""  --> shallow can't copy multi dimenetional array
     --> only deepcopy can do that
     import copy package for that
     

 """

a=[
    [1,2,3],
    [4,5,6]
]

b = copy.deepcopy(a)

a[0][0]=23

print(a)
print(b)