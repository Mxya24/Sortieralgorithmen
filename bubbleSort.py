
l = [1,0,8,5,4,2]
"""015428

"""
n = len(l)

for j in range(n):

    for i in range(n):
        if (l[i]>l[i+1]):
            temp = l[i]
            l[i]=l[i+1]
            l[i+1]=temp

for k in range(len(l)):
    print(l[k])

