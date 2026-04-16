class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = ''.join(filter(str.isalnum,s)).lower()

        for i in range(0,len(stripped)//2):
            if stripped[i] != stripped[(len(stripped)-1) -i]:
                return False
        return True
        