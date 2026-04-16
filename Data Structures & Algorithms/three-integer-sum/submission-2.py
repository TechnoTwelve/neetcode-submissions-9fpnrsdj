class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-1,0,1,2,-1,-4]
        #[-4,-1,-1,0,1,2]
        seen_sum=[]
        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums)-2):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            j = i+1
            k = len(sorted_nums)-1
            while j<k:
                if sorted_nums[j] + sorted_nums[k] + sorted_nums[i] == 0:
                    seen_sum.append([sorted_nums[i],sorted_nums[j],sorted_nums[k]])
                    k-=1
                    j+=1
                    while j < k and sorted_nums[j] == sorted_nums[j-1]:
                        j += 1
                elif sorted_nums[j] + sorted_nums[k] + sorted_nums[i] > 0:
                    k-=1
                elif sorted_nums[j] + sorted_nums[k] + sorted_nums[i] < 0:
                    j+=1
                else:
                    break

        return seen_sum
        