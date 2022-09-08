class Node():
    def __init__(self,value,next_node=None,weight=None):
        self.value=value
        self.next_node=next_node
        self.weight=weight
        
    def __str__(self):
        return str(self.value)
        
    def set_next_node(self,next_node):
        self.next_node=next_node
        
    def get_next_node(self):
        return self.next_node
        
    def get_weight(self,weight):
        return self.weight
        

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


class Queue_with_priority(Queue):
    def __init__(self,len):
        super().__init__(len)
    

    
    def traverse(self):
        
        first=self.head
        while first!=None :
            print("Nodul are valoare " + str(first.value)+" si greutatea :"+str(first.weight))
            
            first=first.get_next_node()
    
    
    def enque(self,node):
        
        
        if self.has_space():
            
            # check node weight
            if self.head==None :
                
                self.tail=node
                self.head=self.tail
                self.actual_len+=1
            else:
                
                #case 1 when node hase a bigger weight than head
                if self.head.weight<node.weight:
                    node.set_next_node(self.head)
                    self.head=node
                    self.actual_len+=1
                #case 2 when you have to check every node
                else:
                
                    first=self.head
                
                    
                
                    while first.get_next_node()!=None and first.get_next_node().weight>node.weight :
                        first=first.get_next_node()
                
                    temp=first.get_next_node()
                    node.set_next_node(temp)
                    first.set_next_node(node)
                
                
                    self.actual_len+=1            
 
        else :
            print( "Queue is out of space: max len is %d  %s "   %(self.actual_len,"please dequeue"  ))
    
    
## Nodes Definition
First=Node(1)
Second=Node(2)
Third=Node(3)
Fourth=Node(4)
Fifth=Node(5)
Sixth=Node(6)
Seventh=Node(7)

#Queue Definition -Non prio FIFO

print("#################Non Prio########################")

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


#Queue Definition -Prio - altering  FIFO (in functie de importanta fiecarui nod)
print("################# Prio ########################")


First_P=Node(value=1,weight=243)
Second_P=Node(value=2,weight=244)
Third_P=Node(value=3,weight=240)
Fourth_P=Node(value=4,weight=242)
Fifth_P=Node(value=5,weight=250)
Sixth_P=Node(value=6,weight=241)
New_Queue_p=Queue_with_priority(5)
print(New_Queue_p.is_empty())
New_Queue_p.enque(First_P)
New_Queue_p.enque(Second_P)
New_Queue_p.enque(Third_P)
New_Queue_p.enque(Fourth_P)
New_Queue_p.enque(Fifth_P)
New_Queue_p.deque()
New_Queue_p.enque(Sixth_P)

print(New_Queue_p.traverse())
