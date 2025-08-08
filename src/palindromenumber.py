class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = x
        rev = 0
        if x < 0:
            return False
        else:
            while num != 0:
                d = num % 10
                rev = rev * 10 + d
                num //= 10
            if x == rev:
                return True
            else:
                return False