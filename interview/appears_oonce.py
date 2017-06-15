"""
Find the element that appears once
Given an array where every element occurs three times, except one element 
which occurs only once. Find the element that occurs once. 
Examples: 
Input: arr[] = {12, 1, 12, 3, 12, 1, 1, 2, 3, 3}
Output: 2
Idea: Keep hash map of elements ocured - after third time occurance - remove element 

form hash map - the only one that is left in HM is the one we are looking for 
- if there are more than one element in HM - input was wrong 
- one check we can do at the begining - if len(array) %3 == 0 - we know it is wrong input
and len has to be at least 4
"""


def appears_once(array):
	# Check array for valid input based on length
	if array in None or len(array) < 4 or len(array) % 3 == 0:
		return False
	count = {}
	for element in array:
		if count .has_key(element):
			if count[element] == 2:
				# remove third occurance
				del (count[element])
			else:
				count[element] += 1
		else:
			count[element] + 1

	if len(count) > 1:
		return False
	# return element left
	return count.keys()[0]