class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # if the string is empty return
        if not s:
            return
        # assign the last character to the variable last
        last = len(s)-1
        
        # loop through the half of the length of the string and 
        # swap the values 1st for last 2nd for one before last and so on 
        for i in range(len(s)//2):
            s[i],s[last-i] = s[last-i],s[i]
        
