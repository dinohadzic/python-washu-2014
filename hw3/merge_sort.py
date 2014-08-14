def merge_sort(list):
	if len(list) <= 1: #If the length of the input is 1, simply return that value
		return list
	else:
		mid = len(list)/2 
		left = list[:mid]
		right = list[mid:]
		
		left = merge_sort(left)
		right = merge_sort(right)
		
		sorted_list = []
		
		i = 0
		j = 0
		
		while i < len(left) and j < len(right): 
			if left[i] < right[j]: #Should the left be smaller than the right, append it to the list
				sorted_list.append(left[i])
				i += 1
			else:
				sorted_list.append(right[j]) #Should the right be smaller than the left, append it to the list
				j += 1
			if i == len(left) or j == len(right): #If the end is reached on the left (or right), extends the list by what's remaining of the right (or left)
				sorted_list.extend(left[i:] or right[j:])	
		return sorted_list		

