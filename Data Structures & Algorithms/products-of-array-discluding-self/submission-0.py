class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        self.prefixLeft = []
        self.prefixRight = []

        totalLeft = 1
        totalRight = 1

        for num in nums:
            self.prefixLeft.append(totalLeft)
            totalLeft = totalLeft * num 

        for num in range(len(nums)-1,-1,-1):
            self.prefixRight.append(totalRight)
            totalRight *= nums[num]

        self.prefixRight.reverse()
        
        return [left * right for left, right in zip(self.prefixLeft, self.prefixRight)]


        