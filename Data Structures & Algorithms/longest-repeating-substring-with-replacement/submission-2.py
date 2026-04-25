class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # use sliding window, and a while loop maintaining k size

        left = 0
        freq = {}
        max_len = 0
        
        for right in range(len(s)):

            if s[right] in freq:
                freq[s[right]] += 1
            else:
                freq[s[right]] = 1
            
            if right - left + 1 - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1
                

            max_len = max(max_len, right - left + 1)
        
        return max_len
            




            


        
     

            
            

            


        