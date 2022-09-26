#퀵 정렬 = 분할 정복 + 재귀 알고리즘 이용
#pivot을 이용하여 pivot보다 작은 값 큰 값으로 나눔

import random
import time

start = time.time()

n = int(input())
arr = []

for i in range(n):
	arr.append(random.randrange(1,n + 1))

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
print(quick_sort(arr))
print("time :", time.time() - start)