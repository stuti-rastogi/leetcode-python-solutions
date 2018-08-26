def wiggleSort(nums):
	# nums - list[int]

	if not nums:
		return

	n = len(nums)
	for i in range(n-1):
		if (i % 2 == 0) and (nums[i] >= nums[i+1]):
			nums[i], nums[i+1] = nums[i+1], nums[i]
		if (i % 2 == 1) and (nums[i] < nums[i+1]):
			nums[i], nums[i+1] = nums[i+1], nums[i]

	print ("Output:\t" + str(nums) + "\n")

nums = [1, 2, 7, 5, 3, 8]
print ("Input:\t" + str(nums))
wiggleSort(nums)

nums = [3, 4, 3, 4, 1, 1, 5]
print ("Input:\t" + str(nums))
wiggleSort(nums)