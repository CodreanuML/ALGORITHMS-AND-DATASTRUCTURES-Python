class Node():
    def __init__(self,value,next_node=None):
        self.value=value
        self.next_node=next_node
        
    def __str__(self):
        return str(self.value)
        
    def set_next_node(self,next_node):
        self.next_node=next_node
        
    def get_next_node(self):
        return self.next_node
        

class Queue():
    def __init__(self,len):
        self.max_len=len
        self.head=None
        self.tail=None
        self.actual_len=0
        
    def __str__(self):
        return ("Queue of length {}".format(str(self.max_len)))
        
    
    def has_space(self):
        return self.actual_len<self.max_len
        
    def is_empty(self):
        if self.actual_len==0 :
            return True
        else :
            return False
        
    def enque(self,node):
        
        if self.has_space():
            if self.head==None :
                
                self.tail=node
                self.head=self.tail
                self.actual_len+=1
            else:
                self.tail.set_next_node(node)
                self.tail=node
                self.actual_len+=1
        else :
            print( "Queue is out of space: max len is %d  %s "   %(self.actual_len,"please dequeue"  ))
            
            
    def traverse(self):
        
        first=self.head
        while first!=None :
            print(first.value)
            first=first.get_next_node()
            
    def deque(self):
        if self.is_empty():
            print("Unable to dequeue , queue is empty")

        else :
            self.head=self.head.get_next_node()
            self.actual_len-=1

    def left_queue(self,node):
        
        first=self.head 
        while first!=None :
            try:
                next=first.get_next_node()
                if next.value==node.value :
                    first.set_next_node(first.get_next_node().get_next_node())
            except AttributeError:
                print("unable to left")

            first=first.get_next_node()


    
## Nodes Definition
First=Node(1)
Second=Node(2)
Third=Node(3)
Fourth=Node(4)
Fifth=Node(5)
Sixth=Node(6)
Seventh=Node(7)

#Queue Definition
New_Queue=Queue(5)
print(New_Queue.is_empty())
New_Queue.enque(First)
print(New_Queue.is_empty())
New_Queue.enque(Second)
New_Queue.enque(Third)
New_Queue.enque(Fourth)
New_Queue.enque(Fifth)
New_Queue.enque(Sixth)
New_Queue.enque(Seventh)


print(New_Queue.traverse())
New_Queue.enque(Sixth)
New_Queue.left_queue(Second)
print(New_Queue.traverse())
