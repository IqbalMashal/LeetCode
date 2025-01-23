class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        self.list = words
        if len(self.list) == 0:
            return ""
        for word in self.list:
            temp = word[::-1]
            if word == temp:
                return word
        return ""