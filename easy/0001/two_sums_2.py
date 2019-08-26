class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    '''
    We want to use a dict method to solve this problem as dict uses hashing to search for the key value pair.
    Search time is constant when averaged while using a appropriate hash function and propotionate alpha.
    We are making a single pass through the entire nums array all the while adding key value pairs to the dictionary we have created.
    '''
        twoSumDict = {} # We use a dictionary to hold the complementary values of each value we are iterating in nums
        for i in range(len(nums)):
            if nums[i] in twoSumDict:
                return [twoSumDict[nums[i]],i]
            else:
                twoSumDict[target - nums[i]] = i 
