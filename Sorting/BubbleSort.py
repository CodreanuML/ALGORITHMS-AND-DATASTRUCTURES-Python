import random
import time



# FUNCTIE DE GENERARE ARRAY DE LUNGIME CERUTA CU RANDOM NUMBERS  --->> GENERATE_ARR
# FUNCTIE CALCUL PERMORMANTA EXECUTIE --->> TIME_EXEC @ DECORATOR
# FUNCTIE SORTARE BUBBLE SORT--->> BUBBLE_SORT




global unsorted_arr
unsorted_arr=[]
def generate_arr(lenarr):
	global unsorted_arr
	unsorted_arr=[]
	for i in range(0,lenarr):

		unsorted_arr.append(random.randint(1,lenarr))
	

def time_exec(function_d):
	print('I STARTED')
	
	def wrapper(*args,**kargs):
		time_enter=time.time()
		print(function_d(*args,**kargs))
		
		time_leaved=time.time()
		duration=time_leaved-time_enter

		print(duration)	
	return wrapper

@time_exec
def bubble_sort(arr):
	for i in range(0,len(arr)):
		for j in range(0,len(arr)-1-i):
			if arr[j]>arr[j+1] :
				arr[j],arr[j+1]=arr[j+1],arr[j]

			

	return arr 



generate_arr(6500)

bubble_sort(unsorted_arr)