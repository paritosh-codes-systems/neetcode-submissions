class MinStack:
   
    def __init__(self):
        self.stacks = []
        self.min_stacks = []
        
    def push(self, val: int) -> None:
        self.stacks.append(val)
        if self.min_stacks:
            val = min(val, self.min_stacks[-1])
        
        self.min_stacks.append(val)
        
           

    def pop(self) -> None:
        self.stacks.pop()
        self.min_stacks.pop()
                

    def top(self) -> int:
        return self.stacks[-1]
        

    def getMin(self) -> int:
       return self.min_stacks[-1]


        
