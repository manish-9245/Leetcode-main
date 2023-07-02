class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        x=[i for i in sentence] 
        b=set(x)
        return len(b)==26