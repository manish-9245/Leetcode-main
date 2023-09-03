class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        a = map(int, list(''.join(map(str, nums))))
        return abs(sum(nums) - sum(a))