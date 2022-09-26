def bs(data, item, low, high):#찾고자 하는 값 item
	if (low > high):
		return -1
	else:
		mid = (low + high) // 2
		if (item == data[mid]):
			return mid
		elif item < data[mid]:
			return bs(data,item,low,mid - 1)
		else:
			return bs(data,item,mid + 1,high)

data = [1, 3, 5, 6, 7, 9 ,10 ,14, 17, 19]
n = 10
location = bs(data,22,0, n-1)
print(location)