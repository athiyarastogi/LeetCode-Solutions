class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        new_string=s.split()
        len_last_element=len(new_string[-1])
        return(len_last_element)
