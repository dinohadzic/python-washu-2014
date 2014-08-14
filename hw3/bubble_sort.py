def bubble_sort(list):
	for i in range(len(list))[::-1][:-1]:
		for j in range(i):
			if list[j] > list[j+1]:
				swap_values = list[j+1]
				list[j+1] = list[j]
				list[j] = swap_values
	return list
    