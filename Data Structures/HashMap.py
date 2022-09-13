Records=[['Lucian','0743095980'],
['Mark'',0743095981'],
['Zarro','0743095982'],
['Terro','0743095983'],
['Feinman','0743095984'],
['Kintaro','0743095985'],
['Criss','0743095986'],
['Ganny','0743095987'],
['Marko','0743095988'],
['Fannuci','0743095989'],]

#First Creating A Hashmap that is unable to handle collisions

class HashMap():
    def __init__(self,len):
        self.len=len
        self.hash_array=[]
        for i in range(0,len):
            self.hash_array.append(None)
            
            
    def __str__(self):
        return str(self.hash_array)
      
      
    def hashing(self,input):
        hashed=0

        
        #creating a hash function for a string position multiplied with ascii char encoding multiplying by  9 number divided by len of arr
        
        for i in input:
            
            position=1 #define position index
            
            ascii_code=ord(i) ##convert utf
            
            hashed+=position*ascii_code*9
        
        hashed=hashed % self.len
        print(hashed)
        return(hashed)
     
    def add_record(self,input):
        hashed_key=0
        hashed_key=self.hashing(input[0])
        if self.hash_array[hashed_key]==None:
            self.hash_array[hashed_key]=input
        else:
            print("Collision Encountered")
       
    def retrieve_record(self,input):
        hashed_key=0
        hashed_key=self.hashing(input)
        if self.hash_array[hashed_key]==None:
            print("Record is not present")
        else :
            recc=self.hash_array[hashed_key]
            if recc[0]==input:
                print("{a} has the phone number {b}".format(a=recc[0],b=recc[1]))
            else :
                print("Record is not present")
       
MyHash=HashMap(5)
print(MyHash)
for i in Records:
    MyHash.add_record(i)
print(MyHash)
MyHash.retrieve_record("Cal")
MyHash.retrieve_record("Lucian")

#############################ADDING A LINK LIST CLASS################################
########################FIRST STEP TO AVOID COLLISIONS###############################


##CREATING A CHAINED HASH MAP USING LINKED LIST
##IMPORTING LINKED LISTE STRUCTURE

class Node():


	def __init__(self,value):
		self.value=value
		self.next_node=None

	def add_next_node(self,node):
		self.next_node=node

	def get_next_node(self):
		return self.next_node

	def __rpr__(self):
		return self.value



class Linked_List():

	def __init__(self):
		self.head=None

	def add(self,Node):
		if self.head==None:

			self.head=Node

		else:

			temp=self.head
			self.head=Node
			self.head.add_next_node(temp)


	def traverse(self):
		node_f=self.head
		while node_f :
			print(node_f.value)
			node_f=node_f.get_next_node()
			
	
	def getnode(self,node):
		node_f=self.head
		while node_f :
			if node_f.value[0]==node:
			    return node_f.value
			node_f=node_f.get_next_node()


class HashMap_collision_linked(HashMap):
    def __init__(self,len):
        self.len=len
        self.hash_array=[]
        for i in range(0,len):
            self.hash_array.append(Linked_List())        
    
    def __str__(self):
        return str(self.hash_array)       
        
        
    def add_record(self,input):
        hashed_key=0
        hashed_key=self.hashing(input[0])
        
        list=self.hash_array[hashed_key]
        
        list.add(Node(input))
        
        
    def get_node_value(self,input):
        hashed_key=0
        hashed_key=self.hashing(input)
        lista=self.hash_array[hashed_key]
        allowed=lista.getnode(input)
        
        
        if allowed !=None :
            print("input gasit  gasit la index {}".format(hashed_key))
            print (str(input)+" are numarul " + str(allowed[1]))
        else:
            print ("Node not found")
            
Hash_map_linked=HashMap_collision_linked(5)
print(Hash_map_linked)
for i in Records:
    Hash_map_linked.add_record(i)

Hash_map_linked.hash_array[1].traverse()
Hash_map_linked.get_node_value('Ganny')
