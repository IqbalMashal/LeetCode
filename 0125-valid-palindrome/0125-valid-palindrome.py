class Solution:
    def isPalindrome(self, s: str) -> bool:
        z = ''.join(filter(str.isalnum(),s)).lower()

       return z == z[::-1]