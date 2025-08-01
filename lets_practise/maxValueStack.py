class maxStack:

    def __init__(self):
        self.stack = []
        self.maxval = []
        #self.size = size
    
    def push(self,val):
        if(len(self.stack) < size):
            self.stack.append(val)
            if not self.maxval or val > self.maxval[-1]:
                self.maxval.append(val)
        else:
            print("stack is full")

    def pop(self):
        if(len(self.stack) == 0):
            print("stack is empty")
        else:
            res = self.stack.pop()
            print("poped value is: ", res)
            if res in self.maxval:
                self.maxval.pop()

    def getmax(self):
        if(len(self.maxval) == 0 ):
            print("stack is empty, so no max element")
        else:
            print(self.maxval[-1])


size = int(input("enter the size of stack: "))
ms = maxStack()
while(1):
    mode = int(input("enter the action: "))
    if(mode == 0):
        val = int(input("enter the element to insert: "))
        ms.push(val)
    elif (mode == 1):
        ms.pop()
    elif (mode ==2):
        ms.getmax()
    else:
        print("exiting")
        break
         
