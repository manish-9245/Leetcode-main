class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count=0
        output = [int(x) for x in str(num)]
        for i in range(len(output)):
            if num%output[i]==0:
                count+=1;
        return count;