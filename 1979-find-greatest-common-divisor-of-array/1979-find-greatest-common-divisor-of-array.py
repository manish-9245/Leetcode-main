class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minn, maxx = min(nums), max(nums)

        for num in range(minn+1, 0, -1):
            if maxx % num == 0 and minn % num == 0:
                return num

        return 1