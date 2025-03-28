class Solution:
	def subarraysDivByK(self, nums: List[int], k: int) -> int:
		d = {0: 1}
		prefix_sum, count = 0, 0

		for num in nums:
			prefix_sum = (prefix_sum + num) % k
			count += d.get(prefix_sum, 0)


			d[prefix_sum] = d.get(prefix_sum, 0) + 1

		return count
            
        