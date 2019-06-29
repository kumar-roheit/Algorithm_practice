"""
Example:  convert 123 to 321
or -123 to -321
1. convert 123 to string 
2. 1,2,3 then reverse the string 
3. and then convert them back to integer
""" 

class Solution:
    def reverse(self, x: int) -> int:
        # check the boundary condition
        if x >= (2**31)-1 or x <= -(2**31):
            return 0
        else:
            # convert the integer to string
            strx = str(x)
            # if the integer is positive simple reverse the string
            if x >= 0:
                revx = strx[::-1]
            # if the integer is negative remove the negative symbol and then reverse 
            else:
                rev_temp = x[1:]
                # reversing the string without the negative sign and adding the negative symbol
                revx = '-' + rev_temp[::-1]
            # checking boundary conversion for the reversed integer
            if int(revx) >= (2**31)-1 or int(revx) <= -(2**31):
                return 0
            else: 
                return int(revx)
                
