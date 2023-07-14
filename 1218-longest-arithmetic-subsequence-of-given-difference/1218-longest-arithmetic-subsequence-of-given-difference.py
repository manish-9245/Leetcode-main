class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        dp = {}
        max_length = 0
        for num in arr:
            if num - difference in dp:
                length = dp[num - difference]
                dp[num] = length + 1
            else:
                dp[num] = 1
            max_length = max(max_length, dp[num])
        return max_length