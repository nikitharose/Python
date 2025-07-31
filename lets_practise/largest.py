size = int(input("Enter the number of elements"))
num = []
for i in range (size):
    num.append(int(input()))

num.sort()

print("largest number is: ", num[size-1])
