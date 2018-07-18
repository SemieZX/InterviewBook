class MyStack1:
    def __init__(self):
        self.stackData = []
        self.stackMin = []
    
    def push(self,newNum):
        self.stackData.append(newNum)
        if len(self.stackMin) == 0 or newNum <= self.getMin():
            self.stackMin.append(newNum)
    
    def pop(self):
        if len(self.stackData) == 0:
            raise Exception("your stack is empty!")
        value = self.stackData.pop()
        if value == self.getMin():
            self.stackMin.pop()
        return value
    
    def getMin(self):
        if len(self.stackMin) == 0:
            raise Exception("your stack is empty!")
        return self.stackMin[-1]



class MyStack2:
    def __init__(self):
        self.stackData = []
        self.stackMin = []
    
    def push(self,newNum):
        self.stackData.append(newNum)
        if len(self.stackMin) == 0 or newNum < self.getMin():
            self.stackMin.append(newNum)
        else:
            self.stackMin.append(self.getMin())
    
    def pop(self):
        if len(self.stackData) == 0:
            raise Exception("it's empty")
        self.stackMin.pop()
        return self.stackData.pop()

        
        
    def getMin(self):
        if len(self.stackMin) == 0:
            raise Exception("it's empty")
        return self.stackMin[-1]