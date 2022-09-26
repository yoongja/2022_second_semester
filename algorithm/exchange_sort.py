import random
import time

start = time.time()
n = int(input())
arr = []

for i in range(n):
	arr.append(random.randrange(1,n + 1))

def exchange_sort(arr,n):
	for i in range(n):
		for j in range(0, n - i -1):#배열의 총 크기에서 i의 값과 1을 뺀 만큼 반복
			if arr[j] > arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]
exchange_sort(arr,n)
print(arr)
print("time :", time.time() - start)