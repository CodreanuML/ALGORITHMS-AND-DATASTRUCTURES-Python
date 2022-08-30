class Node():
    def __init__(self,add_value=None):
        self.value=add_value
        self.next_node=None
        
    def set_val(self,changed_val):
        self.value=changed_val
        
    def set_next_node(self,next_node_v):
        self.next_node=next_node_v
    
    def get_next_node(self):
        return self.next_node
        
    def __str__(self):
        return str(self.value)
        

class Stack():
    def __init__(self,length_a):
        self.length=length_a
        self.head=None
        self.length_count=0
        
    def push(self,value):
        if self.head==None :
            self.head=value
            self.length_count+=1
        elif self.length>self.length_count:
            value.set_next_node(self.head)
            self.head=value
            self.length_count+=1
        elif self.length<=self.length_count:
            print("stack_overflow")
            
    def pop(self):
        self.head=self.head.get_next_node()
        
        
    def traverse(self):
        first=self.head
        print(first.value)
        while first.get_next_node() != None:
            first=first.get_next_node()
            print(first.value)
  
