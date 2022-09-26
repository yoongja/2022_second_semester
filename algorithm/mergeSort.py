#배열을 나눌 수 없을때 까지 최대한 분할, 
#병합하며 점점 큰 배열을 만들어 나가기
#기저 조건은 배열의 크기가 2보다 작을때
#배열의 크기가 2보다 작을때는 배열을 그대로 반환
#정수 n, 크기가 n인 배열 arr

def mergeSort(arr):#n은 arr의 크기
	size = len(arr)
	if size <= 1 :
		return arr
	mid = len(arr) // 2
	left = mergeSort(arr[:mid])
	right = mergeSort(arr[mid:])
	merged = merge(left,right)
	return merged

def merge(left, right):
	merged = []
	while len(left) > 0 and len(right) > 0:
		if left[0] <= right[0]:
			merged.append(left.pop(0))
		else:
			merged.append(right.pop(0))
	if len(left) > 0:
		merged += left
	if len(right) > 0:
		merged += right

	return merged
			
arr = [3, 5, 2, 9, 10, 14, 4, 8]
arr = mergeSort(arr)
print(arr)