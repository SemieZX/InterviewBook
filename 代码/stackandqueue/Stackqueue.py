class TwoStackQueue:
    def __init__(self):
        self.stackPush = []
        self.stackPop = []
    def add(self,newNum):
        self.stackPush.append(newNum)
    
    def poll(self):
        if len(self.stackPop) == 0 and len(self.stackPush) == 0:
            raise Exception("it's empty")
        elif len(self.stackPop) == 0:
            while len(self.stackPush) != 0 :
                self.stackPop.append(self.stackPush.pop())
        return self.stackPop.pop()
    
    def peek(self):
        if len(self.stackPop) == 0 and len(self.stackPush) == 0:
            raise Exception("it's empty")
        elif len(self.stackPop) == 0:
            while len(self.stackPush) != 0:
                self.stackPop.append(self.stackPush.pop())
        return self.stackPop[-1]
    