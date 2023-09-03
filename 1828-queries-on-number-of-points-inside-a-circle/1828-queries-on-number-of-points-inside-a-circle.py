class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answers=[]
        for j in range (len(queries)):
            count=0
            for i in range (len(points)):
                if math.sqrt((queries[j][0]-points[i][0])**2+(queries[j][1]-points[i][1])**2)<=queries[j][2]:
                    count+=1
            answers.append(count)
        return answers