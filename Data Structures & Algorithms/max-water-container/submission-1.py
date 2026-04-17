class Solution:
    def maxArea(self, heights: List[int]) -> int:

        area = 0
        i = 0
        j = len(heights)-1

        while i < j:
            height = min(heights[i],heights[j])
            area = max(area,(height)*(j-i))

            if heights[i] > heights[j]:
                j-=1
            elif heights[i] < heights[j]:
                i+=1
            else:
                i+=1

        return area

            

            

    
        

            

            