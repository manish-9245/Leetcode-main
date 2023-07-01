class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bit=0
        ele=0
        for i in range(0,max(nums)):
            if i not in nums:
                bit+=1;
                ele=i;
        if bit==0:
            return max(nums)+1
        elif ele==0:
            return 0
        else:
            return ele