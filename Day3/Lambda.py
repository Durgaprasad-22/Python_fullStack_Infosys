a=[2,3,4,5,6,7]

print("usiing lambda and ternary operator")
print(list(map((lambda num: f"{num} is even" if num%2==0 else f"{num} is odd"),a)))


def even(num):
    if num%2==0:
        return f"{num} is even"
    # else:
    #     return f"{num} is odd"

result=list(map(even,a))


print("usiing map func")
print(result)

result2=list(filter(even,a))
print("usiing filter func")
print(result2)
