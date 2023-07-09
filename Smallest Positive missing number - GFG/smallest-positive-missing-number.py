#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,nums,n):
        #Your code here
        if 1 in nums:
            nums.sort()
            for i in range(0, n - 1):
                if nums[i + 1] != nums[i] + 1 and nums[i + 1] != nums[i]:
                    if nums[i] + 1 > 0:
                        return nums[i] + 1
            return nums[n - 1] + 1
        else:
            return 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math


def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            print(ob.missingNumber(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends