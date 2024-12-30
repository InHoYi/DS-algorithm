from typing import Sequence

def bubbleSort(aList : Sequence) -> Sequence:
	for i in range(len(aList) - 1, 0, -1):
		for j in range(i):
			if aList[j] > aList[j + 1]:
				aList[j], aList[j + 1] = aList[j + 1], aList[j]

	return aList