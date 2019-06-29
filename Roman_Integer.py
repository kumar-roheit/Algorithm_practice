class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary for conversion 
        conversion = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        num = 0
        # 1. I + V will become 6 whereas should be 4 similarly for I + X
        if 'IV' in s or 'IX' in s:
            num -= 2
        # 2. X can be placed before L (50) and C (100) to make 40 and 90 (similar logic from 1 applies)
        if 'XL' in s or 'XC' in s:
            num -= 20
        # 3. C can be placed before D (500) and M (1000) to make 400 and 900 (similar logic from 1 applies)
        if 'CD' in s or 'CM' in s:
            num -= 200
        # add up all the numbers    
        for char in s:
            num += conversion[char]
        return num
