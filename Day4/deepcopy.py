import copy

a=[
    [1,2,3],
    [4,5,6]
]

b = copy.deepcopy(a)

a[0][0]=23

print(a)
print(b)