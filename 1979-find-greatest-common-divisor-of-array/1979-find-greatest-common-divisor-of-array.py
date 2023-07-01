class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
 
        # Everything divides 0
            if (a == 0):
                return b
            if (b == 0):
                return a
 
            # Base case
            if (a == b):
                return a
 
        # a is greater
            if (a > b):
                return gcd(a-b, b)
            return gcd(a, b-a)
        return gcd(max(nums),min(nums))