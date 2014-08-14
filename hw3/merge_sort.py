def merge_sort(list):
	if len(list) <= 1:
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
			if left[i] < right[j]:
				sorted_list.append(left[i])
				i += 1
			else:
				sorted_list.append(right[j])
				j += 1
			if i == len(left) or j == len(right):
				sorted_list.extend(left[i:] or right[j:])	
		return sorted_list		

