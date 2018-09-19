class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        head = 0
        max_length = 0
        for tail in range(len(s)):
            if s[tail] in s[head:tail]:
                max_length = max(max_length, tail-head)
                head = s[head:tail].index(s[tail])+1+head
        max_length = max(max_length, len(s)-head)
        return max_length
