str = input("Enter the string: ")
num = []
size = int(input("Enter the number of elements: "))
for i in range (size):
    num.append(int(input()))

print("Reversed list is : ", num[::-1])


#slicing the string in reverse
print ("Reversed string is : ",str[::-1])
