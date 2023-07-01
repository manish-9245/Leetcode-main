class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            res.append(abs(sum(nums[0:i])-sum(nums[i+1:])))
        return res