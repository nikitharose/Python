class buffer:
    def __init__(self, size):
        self.size = size
        self.queue = [None]*self.size
        self.counter = 0
        self.head = 0
        self.tail = 0

    def enqueue(self, val):
        if ( self.counter == self.size):
            print("The queue is full")
        else:
            self.queue[self.head] = val
            self.counter = (self.counter+1)
            self.head = (self.head+1)%(self.size)
    
    def dequeue(self):
        if (self.counter == 0):
            print("Queue is empty")
        else:
            res = self.queue[self.tail]
            self.queue[self.tail]=None
            self.tail = (self.tail+1)% (self.size)
            return res 
            self.counter = self.counter-1;   

    def peek(self):
        if(self.counter == 0):
            print("No element to peek")
        else:
            res = self.queue[self.tail]
            print(res) 

size = int(input("enter the size of buffer: "))
bf = buffer(size)

while (1):
    mode = int(input("Enter the opertaion: "))
    if(mode == 0):
        val = int(input("enter the value"))
        bf.enqueue(val)
    elif (mode ==1):
        res=bf.dequeue()
        print(res)
    elif(mode == 2):
        bf.peek()
    else:
        print("wrong operation")
        break  
