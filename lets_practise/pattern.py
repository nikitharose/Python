num = int(input("enter the levels: "))
for i in range (1,num+1):
    print(i*'* ')

for i in range (1,num+1):
    print(" " * (num - i)*2+"".join(str(j)+" " for j in range(1,1+i))+"".join(str(j)+" " for j in range(i-1, 0 ,-1)))
   
