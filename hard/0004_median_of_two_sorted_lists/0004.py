# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 12:33:39 2019

@author: naveenpc
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        ans = 0
        combinedList = nums1 + nums2
        combinedList.sort()
        return ((combinedList[(len(combinedList)-1)//2] + combinedList[len(combinedList)//2])/2)
        
        
        
assert(Solution().findMedianSortedArrays([1,3],[2]) == 2.0)
assert(Solution().findMedianSortedArrays([1,2],[3,4]) == 2.5)
