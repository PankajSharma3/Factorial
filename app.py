# def new_func(a):
#     f=1
#     for i in range(a):
#             f=f*(i+1)
#     return (f)
# b=int(input())
# print(new_func(b))
def new_func(a):
        if a==1:
                return 1
        else:
                return a + (a+1)
b=int(input())
print(new_func(b))
