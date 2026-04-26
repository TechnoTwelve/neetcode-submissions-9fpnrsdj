class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        have = 0
        need = Counter(t)
        window = {}
        res = (-1, -1)
        res_len = float("inf")

        for right in range(len(s)):
            if s[right] in window:
                window[s[right]] += 1
            else:
                window[s[right]] = 1

            if window[s[right]] == need[s[right]]:
                have += 1

            while have == len(need):
                if (right - left + 1) < res_len:
                    res_len = right - left + 1
                    res = (left, right)
                if s[left] in window:
                    window[s[left]] -= 1
                if window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""