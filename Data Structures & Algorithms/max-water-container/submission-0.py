class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # to work out area we need the height and the length
        # for length we could use the difference between iteration

        area = 0

        for i in range(len(heights) - 1):
            j = len(heights) - 1
            while j>0:
                height = heights[i] if heights[i] < heights[j] else heights[j] 
                area = max(area,(height)*abs((i-j)))
                j-=1
        return area
            



        