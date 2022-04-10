def merge():

	list1 = input("Enter the elements for List 1:").split()
	for i in range(len(list1)):
		 list1[i] = eval(list1[i])

	list2 = input("Enter the elements for List 2:").split()
	for i in range(len(list2)):
		 list2[i] = eval(list2[i])

	size1 = len(list1)
	size2 = len(list2)

	res = []
	i, j = 0, 0

	#union of sorted lists

	while i < size1 and j < size2:
		if list1[i] < list2[j]:
			res.append(list1[i])
			i += 1

		else:
			res.append(list2[j])
			j += 1

	res = res + list1[i:] + list2[j:]

	# print output
	print ("The merged list is: " + str(res))

	#Reference Links
	#
	# https://snakify.org/tr/lessons/lists/
	# https://www.w3schools.com/python/gloss_python_join_lists.asp
	#

merge()

