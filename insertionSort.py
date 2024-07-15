l = [1,0,8,5,4,2]
n= len(l)

for j in range(1,n):
    i = j
    while l[i]<l[i-1]:
        
        temp = l[i]
        l[i]=l[i-1]
        l[i-1]=temp

        if (i!=1):
            i -= 1
    

for k in range(n):
    print(l[k])