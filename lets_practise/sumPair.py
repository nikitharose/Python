num = int(input("enter the number of elements: "))
arr = []
temp = 0
for i in range(num):
    arr.append(int(input("enter the number: ")))
    temp =temp+arr[i]
res = set()
sum = int(input("enter the sum: "))
for i in arr:
    if (sum - i) in arr:
        res.add(tuple(sorted((i , sum-i))))

print(res)
