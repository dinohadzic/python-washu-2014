def bubble_sort(list):
	for i in range(len(list))[::-1][:-1]:
		for j in range(i):
			if list[j] > list[j+1]:	#Should the preceding value be greater
				(list[j], list[j+1]) = (list[j+1], list[j]) #Switches the values so that the smaller value precedes the larger one.
	return list
    