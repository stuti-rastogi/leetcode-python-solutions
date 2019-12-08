class Solution(object):
	def threeSum(self, nums):
		res = []
		nums.sort()
		length = len(nums)

		# skip the last two as they have been taken into account
		for i in range(length-2):
			# min number can't be positive, since 3 +ve numbers can't make 0
			if nums[i]>0:
				break

			# don't repeat calculations for repeated number
			if i>0 and nums[i]==nums[i-1]:
				continue

			# starting left and right
			# always start with i+1, considering case i=0
			l, r = i+1, length-1
			while l<r:
				total = nums[i]+nums[l]+nums[r]
				if total<0:
					l= l + 1
				elif total>0:
					r = r - 1
				else:
					# total = 0
					res.append([nums[i], nums[l], nums[r]])

					# skip repeats
					while l<r and nums[l]==nums[l+1]:
						l = l + 1
					while l<r and nums[r]==nums[r-1]:
						r = r - 1

					l = l + 1
					r = r - 1
		return res