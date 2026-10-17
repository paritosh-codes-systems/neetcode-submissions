class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stacks_ops = []
        for (idx, ops)in enumerate(operations):
            if ops == "+" : 
                stacks_ops.append(stacks_ops[-1] +  stacks_ops[-2])
            elif ops == "D" :
               stacks_ops.append(2* stacks_ops[-1])
            elif ops == "C":
               stacks_ops.pop() 
            else:
              stacks_ops.append(int(ops))

        
        print(stacks_ops)
        return sum(stacks_ops)