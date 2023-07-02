class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        res=0
        rule=0
        if ruleKey=="type":
            rule=0
        elif ruleKey=="color":
            rule=1
        else:
            rule=2
        for i in range(len(items)):
            if items[i][rule]==ruleValue:
                res+=1
        return res