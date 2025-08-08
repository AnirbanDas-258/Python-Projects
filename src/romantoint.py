class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        value = [1, 5, 10, 50, 100, 500, 1000]
        roman_dict = dict(zip(symbols, value))
        
        total = 0
        prev_value = 0 
        for char in s:
            current_value = roman_dict[char]
            if current_value > prev_value:
                total += current_value - 2 * prev_value
            else:
                total += current_value
            prev_value = current_value
        
        return total
solution = Solution()
print(solution.romanToInt("III"))# Output: 3
print(solution.romanToInt("LVIII"))# Output: 58
print(solution.romanToInt("MCMXCIV"))# Output: 1994

