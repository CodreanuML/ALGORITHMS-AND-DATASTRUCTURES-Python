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
            
    def returnNodes(self):
        returned_nodes=[]
        first=self.head
        while first!=None :
            returned_nodes.append(first)
            first=first.get_next_node()
        return returned_nodes 
         
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


print("################ Warehouse ##################")
#Creating a manager to handles a Warehouse with 3 shelfs



class WareHouse():
    def __init__(self):
        self.row1=Queue(3)
        self.row2=Queue(3)
        self.row3=Queue(3)

        self.rows_no_p=[self.row1,self.row2,self.row3]

        
    def enque_a_product(self,product):
        
        # check if has weight or not to select the row 
       
        for row in self.rows_no_p :
            if row.has_space():
                row.enque(product)
                break
            
    
    
    def deque_a_row_no_prio(self):
        first_row=self.row1
        
        try:  
            if first_row.head.value != None :
            
                while True:
                    first_row.deque()
                    try:
                        first_row.head.get_next_node()
                    except AttributeError :
                        break
        except AttributeError:
            print("Warehouse empty")
            
        second_row=self.row2        
    
    
        try:    
            if second_row.head.value != None :
            
                nodes=second_row.returnNodes()
                for node in nodes :
                    self.row1.enque(node)
                while True:
                    second_row.deque()
                    try:
                        second_row.head.get_next_node()
                    except AttributeError :
                        break
        except AttributeError:
            pass
 
 
        third_row=self.row3        
    
    
        try:    
            if third_row.head.value != None :
            
                nodes=third_row.returnNodes()
                for node in nodes :
                    self.row2.enque(node)
                while True:
                    third_row.deque()
                    try:
                        third_row.head.get_next_node()
                    except AttributeError :
                        break
        except AttributeError:
            pass
         
         
           
My_WareH=WareHouse()

Product1=Node(1)
Product2=Node(2)
Product3=Node(3)
Product4=Node(4)
Product5=Node(5)
Product6=Node(6)
Product7=Node(value=7,weight=241)
Product8=Node(8)
Product9=Node(9)
Product10=Node(10)
Product11=Node(value=11,weight=242)
Product12=Node(value=12,weight=240)
Product13=Node(value=13,weight=239)
My_WareH.enque_a_product(Product1)
My_WareH.enque_a_product(Product2)
My_WareH.enque_a_product(Product3)
My_WareH.enque_a_product(Product4)
My_WareH.enque_a_product(Product5)
My_WareH.enque_a_product(Product6)
My_WareH.enque_a_product(Product7)
My_WareH.enque_a_product(Product8)
My_WareH.enque_a_product(Product9)
My_WareH.enque_a_product(Product10)
My_WareH.enque_a_product(Product11)
My_WareH.enque_a_product(Product12)
My_WareH.enque_a_product(Product13)


print("####row1###")
My_WareH.row1.traverse()
print("####row2###")
My_WareH.row2.traverse()
print("####row3###")
My_WareH.row3.traverse()
print("####row4###")

print("################ After Deque ##################")

My_WareH.deque_a_row_no_prio()
My_WareH.deque_a_row_no_prio()
My_WareH.deque_a_row_no_prio()
My_WareH.deque_a_row_no_prio()
print("####row1###")
My_WareH.row1.traverse()
print("####row2###")
My_WareH.row2.traverse()
print("####row3###")
My_WareH.row3.traverse()

