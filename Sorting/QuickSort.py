import random
import datetime ,time


# FUNCTIE DE GENERARE ARRAY DE LUNGIME CERUTA CU RANDOM NUMBERS  --->> GENERATE_ARR
# FUNCTIE CALCUL PERMORMANTA EXECUTIE --->> TIME_EXEC @ DECORATOR ---(AFLA CUM SE FOLOSESTE CU  O FUNCTIE RECURSIVA)
# FUNCTIE SORTARE QUICK SORT--->> Quicksort



global array_unsorted
array_unsorted=[]
def generate_arr(arr_len):
	global array_unsorted
	for i in range(0,arr_len):
		array_unsorted.append(random.randint(0,arr_len))
	print(array_unsorted)

def time_exec(function):
	def wrapper(*args,**kargs):
		time1=time.time()
		function(*args,**kargs)
		time2=time.time()
		print(time2-time1)
	return wrapper

def partition(arr,l,r):
	j=l-1
	pivot=r
	for i in range(l,r):
		if arr[i]<arr[pivot]:
			j=j+1
			
			arr[j],arr[i]=arr[i],arr[j]

		
			
	arr[j+1],arr[pivot]=arr[pivot],arr[j+1]

	
	return j+1


def quicksort(arr,l,r):
	
	if l<r :
		mid=partition(arr,l,r)
		quicksort(arr,l,mid-1)
		quicksort(arr,mid+1,r)



generate_arr(6500)

print(quicksort(array_unsorted,0,6499))
print(array_unsorted)