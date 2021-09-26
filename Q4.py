class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        len_=0
        
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[len_]=nums[i]
                len_+=1
        
        return(len_)
                
    
        
