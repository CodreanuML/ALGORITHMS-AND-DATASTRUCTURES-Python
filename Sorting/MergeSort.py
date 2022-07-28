
import random
import datetime ,time


# FUNCTIE DE GENERARE ARRAY DE LUNGIME CERUTA CU RANDOM NUMBERS  --->> GENERATE_ARR
# FUNCTIE CALCUL PERMORMANTA EXECUTIE --->> TIME_EXEC @ DECORATOR ---(AFLA CUM SE FOLOSESTE CU  O FUNCTIE RECURSIVA)
# FUNCTIE SORTARE MERGE SORT--->> MERGE_SORT



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


def merge_arr(left,right):
	m=len(left)
	n=len(right)
	z=m+n
	arr=[]
	for i in range(0,z):
		arr.append(0)
	i=0
	j=0
	k=0	
	while (i< m and j < n ):
		if left[i]<right[j]:
			arr[k]=left[i]
			i+=1
			k+=1

		elif left[i]>=right[j]:
			arr[k]=right[j]
			j+=1
			k+=1

	while i<m:
		arr[k]=left[i]
		i+=1
		k+=1
	while j<n:
		arr[k]=right[j]
		j+=1
		k+=1

	return arr


def mergesort(arr):
	if len(arr)<2:
		return arr

	else:
		mid=len(arr)//2
		
		left=mergesort(arr[0:mid])
		right=mergesort(arr[mid:len(arr)])


	return merge_arr(left,right)


generate_arr(6500)

print(mergesort(array_unsorted))