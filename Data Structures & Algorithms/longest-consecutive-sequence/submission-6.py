class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cons = set(nums)
        count = 0
        longest = 0

        #[1,2,3,9,10,11,12]

        for num in cons:
            if num-1 not in cons:
                count = 1
                while num + count in cons:
                    count+=1
                longest = max(longest,count)
            
        return 0 if not nums else longest
        