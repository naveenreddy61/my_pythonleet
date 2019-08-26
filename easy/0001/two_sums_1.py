class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # Here we have used a brute forece method to iterate through all possible combinations
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    return([i,j])
