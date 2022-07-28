import random
import time



# FUNCTIE DE GENERARE ARRAY DE LUNGIME CERUTA CU RANDOM NUMBERS  --->> GENERATE_ARR
# FUNCTIE CALCUL PERMORMANTA EXECUTIE --->> TIME_EXEC @ DECORATOR
# FUNCTIE SORTARE SELECTION SORT--->> SELECTION_SORT




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
def selection_sort(arr):
	for i in range(0,len(arr)):
		pivot=i
		for j in range(i+1,len(arr)):
			if arr[j]<arr[pivot]:
				pivot=j

		arr[i],arr[pivot]=arr[pivot],arr[i]

	return arr



generate_arr(6500)

selection_sort(unsorted_arr)