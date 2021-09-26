class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            result = target-nums[i]
            for j in range(i+1, len(nums)):
                if nums[j]==result:
                    return (i,j)
            
            
            
 OR

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                result=0
                result+=nums[i]+nums[j]
                if result==target:
                    return(i, j)
