from typing import Sequence

# Selection Sort
# 검색 위치를 지정하여 검색
def selectionSort(aList : Sequence) -> Sequence:

	for i in range(len(aList) - 1):
		minValue = min(aList[i:])
		# 검색 위치 지정
		minValueIndex = aList.index(minValue, i)

		aList[i], aList[minValueIndex] = aList[minValueIndex], aList[i]
	
	result = aList

	return result


t = [43,4,5,3,2,4,32,23,3]
r = selectionSort(t)

print(r)