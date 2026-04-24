class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        longest_substring = 0
        seen = {}

        for right in range(len(s)):
            if s[right] in seen:
                left = max(left,seen[s[right]] + 1)

            longest_substring = max(longest_substring, (right - left + 1))
            seen[s[right]] = right
        
        return longest_substring




