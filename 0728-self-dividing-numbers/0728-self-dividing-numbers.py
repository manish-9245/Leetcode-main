class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for i in range(left, right+1):
            if "0" in str(i):
                continue
            val = i
            while val > 0:
                n = val % 10
                if i % n != 0:
                    val = -1
                val = val // 10
            if val != -1:
                result.append(i)
        return result
