class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        number_string=str(x)
        num_str=""
        for i in number_string:
            if i.isdigit():
                num_str=num_str+i
        rev_str=num_str[::-1]
        
        if number_string[0]=="-":
            rev_str="-"+rev_str
            
        if -2147483648 <= int(rev_str) <= 2147483647:
            return int(rev_str)
        else:
            return 0
