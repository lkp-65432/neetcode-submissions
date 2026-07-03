class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []

        for c in s.lower():
            if c.isalnum():
                chars.append(c)

        return chars == chars[::-1]


