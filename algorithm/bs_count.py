from unittest.util import _count_diff_hashable


def bs(data, item, low, high,count):#찾고자 하는 값 item
	if (low > high):
		return count
	else:
		mid = (low + high) // 2
		if (item == data[mid]):
			return count
		elif item < data[mid]:
			return bs(data,item,low,mid - 1,count + 1)
		else:
			return bs(data,item,mid + 1,high,count + 1)

data = [1, 3, 5, 6, 7, 9 ,10 ,14, 17, 19]
n = 10
count = 0
count = bs(data,10,0, n-1,count)
print(count)