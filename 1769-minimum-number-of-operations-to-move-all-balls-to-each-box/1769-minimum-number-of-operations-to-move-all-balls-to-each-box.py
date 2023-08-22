class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        indices_object = re.finditer(pattern='1', string=boxes)
        indices = [index.start() for index in indices_object]
        res=[]
        for i in range(0,len(boxes)):
            sum=0
            for j in range(0,len(indices)):
                sum+=abs(i-indices[j])
            res.append(sum)
        return res