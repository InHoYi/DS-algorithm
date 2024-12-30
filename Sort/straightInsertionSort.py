from typing import Sequence

def straightInsertionSort(aList : Sequence) -> Sequence:
	for i in range(1, len(aList)):
		for j in range(i):
			if aList[j] > aList[i]:
				aList[j], aList[i] = aList[i], aList[j]

	return aList