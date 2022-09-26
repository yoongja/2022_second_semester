import random
import time

start = time.time()
exchange_arr = []
quick_arr = []

for i in range(5000):
	exchange_arr.append(random.randrange(1,5000 + 1))
	quick_arr.append(random.randrange(1,5000 + 1))
def exchange_sort(arr,n):
	for i in range(n):
		for j in range(0, n - i -1):#배열의 총 크기에서 i의 값과 1을 뺀 만큼 반복
			if arr[j] > arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]

def quick_sort(arr):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(arr) <= 1:
        return arr

    pivot = arr[0] # 피벗은 첫 번째 원소
    tail = arr[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
	#현재의 피벗값을 포함하고 있는 리스트를 이어서 붙여줌
exchange_sort(exchange_arr,5000)
print(f'exchange_arr : {exchange_arr}')
print(f'quick_arr: {quick_sort(quick_arr)}')

quick_arr = []
exchange_arr = []

for i in range(10000):
	exchange_arr.append(random.randrange(1,10000 + 1))
	quick_arr.append(random.randrange(1,10000 + 1))
exchange_sort(exchange_arr,10000)
print(f'exchange_arr : {exchange_arr}')
print(f'quick_arr: {quick_sort(quick_arr)}')
