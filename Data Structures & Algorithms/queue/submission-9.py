class Deque:
    
      
    def __init__(self):
        self.items = []

    def isEmpty(self) -> bool:
        return len(self.items) ==0

    def append(self, value: int) -> None:
        self.items.append(value)
        

    def appendleft(self, value: int) -> None:
        self.items = [value] + self.items

    def pop(self) -> int:
        current_length = self._length()
        last_index = current_length -1
        if (self._length()>0):
            last_item = self.items[last_index]
            self.items = self.items[:last_index]
            return last_item
        else:
            return -1    
        
        

    def popleft(self) -> int:
        if self._length() ==0 :
            return -1
        first_item = self.items[0]
        self.items = self.items[1:]
        return first_item
        
    def _length(self) -> int: 
        return len(self.items)