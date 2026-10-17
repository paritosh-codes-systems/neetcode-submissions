class Node:
    def __init__(self, val, next_node=None):  # Made next_node optional with default None
        self.val = val
        self.next = next_node
    
    def __str__(self):
        # Prevent infinite recursion if list is long or cyclic
        return f"{self.val} -> {self.next}"

class LinkedList:
    def __init__(self):
        self.node = None  # Acts as the head pointer

    def get(self, index: int) -> int:
        counter = 0
        current_node = self.node
        
        # Traverse until we reach the index or fall off the list
        while current_node is not None:
            if counter == index:
                return current_node.val
            counter += 1
            current_node = current_node.next
            
        return -1  # Index out of bounds or empty list

    def insertHead(self, val: int) -> None:
        # Create a new node pointing directly to the current head
        new_node = Node(val, self.node)
        self.node = new_node

    def insertTail(self, val: int) -> None:
        new_tail = Node(val, None)
        
        # If the list is empty, the new tail becomes the head
        if self.node is None:
            self.node = new_tail
            return
            
        current_node = self.node
        while current_node.next is not None:
            current_node = current_node.next
            
        current_node.next = new_tail

    def remove(self, index: int) -> bool:
        if self.node is None:
            return False
            
        # Special case: removing the head node
        if index == 0:
            self.node = self.node.next
            return True
            
        counter = 0
        current_node = self.node
        
        # Traverse to find the node right BEFORE the one we want to remove
        while current_node is not None and counter < index - 1:
            current_node = current_node.next
            counter += 1
            
        # If the index is out of bounds or the next node doesn't exist
        if current_node is None or current_node.next is None:
            return False
            
        # Bypass the target node
        current_node.next = current_node.next.next
        return True

    def getValues(self) -> List[int]:
        current = self.node
        arr = []
        while current is not None:
            arr.append(current.val)  # Fixed typo: changed array to arr
            current = current.next
        return arr  # Fixed: return the filled list instead of current (None)