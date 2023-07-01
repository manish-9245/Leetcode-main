class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        b = []
        for i in range(0,len(nums)):
            b.insert(index[i],nums[i])
        return b