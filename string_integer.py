class Solution:
    def myAtoi(self, str: str) -> int:
        # an empty variable to store the final number 
        num=''
        
        # remove the leading white spaces
        str = str.lstrip(' ')
        
        if (not str):
            return 0
        
        # if the first element is the - or + sign add it to the number 
        if (str[0]=='-' or str[0]=='+'):
            num = str[0]
            str = str[1:]
            
        # check if the character entered is a number or not 
        for character in str:
            if (character.isdigit()):
                num += character
            else:
                break
        # exception handling                   
        try:
            number = int(num)
            if (number.bit_length() >= 32):
                return (2**31 -1) if number > 0 else  (-2**31)
            return number
        except ValueError:
            return 0
