class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        numbers = [('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000), 
                   ('IV', 4), ('IX', 9), ('XL', 40), ('XC', 90), ('CD', 400), ('CM', 900)]
        
        numbers.sort(key=lambda item: item[1]) 
        
        roman_nums = []
        while num:
            best = numbers[-1]
            for i in range(len(numbers) - 1):
                if numbers[i+1][1] > num:
                    best = numbers[i]
                    break
            
            num -= best[1]
            roman_nums.append(best[0])
            
        return ''.join(roman_nums)
