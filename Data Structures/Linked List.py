


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


	def insert_after(self,Node,value_i):
		node_f=self.head
		while node_f.value != value_i :
			if node_f.get_next_node() == None :
				print("This node is not present")
				break

			node_f=node_f.get_next_node()
		if node_f.value == value_i:
			Node.add_next_node(node_f.get_next_node())
			node_f.add_next_node(Node)


	def insert_before(self,Node,value_i):
		node_f=self.head
		while node_f.value != value_i :
			
			if node_f.get_next_node() == None :
				print("This node is not present")
				break


			if node_f.get_next_node().value == value_i :
			
				break

			node_f=node_f.get_next_node()



		if node_f.get_next_node().value == value_i :
			Node.add_next_node(node_f.get_next_node())
			node_f.add_next_node(Node)




First=Node(1)
Second=Node(2)
Third=Node(3)
Second_1=Node(2.1)
Second_2=Node(2.2)
Fourth=Node(4)
Second_3=Node(2.05)
List=Linked_List()
List.add(First)
List.add(Second)
List.add(Third)
List.insert_after(Second_1,2)
List.insert_after(Second_2,2.1)
List.add(Fourth)
List.insert_before(Second_3,2.1)



List.traverse()