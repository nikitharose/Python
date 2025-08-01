def push(value):
    print("length of arr: ",len(arr), size)
    if(len(arr) < size):
        arr.append(value)
    else:
        print("stack is full")



def pop():
    
    if(len(arr) == 0):
        print("stack is empty:")
    else:
        res = arr[len(arr)-1]
        arr.pop()
        print(" poped value is :", res)

def peek(arr):
    if(len(arr) == 0):
        print("No element present:")
    else:
        print(arr[len(arr)-1])

#main program

size = int(input("enter the size of stack: "))
arr = []
while (1):
    mode = int(input("what is the action: "))
    if(mode == 0):
        val = int(input("enter the value to insert: "))
        push(val)
    elif(mode == 1):
        pop()
    elif(mode == 2):
        peek(arr)
    else:
        print("No valid action")
        break
    
