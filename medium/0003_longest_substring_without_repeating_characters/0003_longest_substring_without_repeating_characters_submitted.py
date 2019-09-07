# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 12:25:27 2019

@author: naveenpc
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        longest = 0
        ans = 0 
        d = dict()
        #cycle through all the elements of the string
        #if the character is not present in the diction we can 
        #append this to the longeset string without any problem
        #problem comes when we encounter a char which is already inside from start to current index.
        #in such a case we need to go back to the index next to the repeated one. and our longest string gets reduced from the next 
        for index,each in enumerate(s):
            if each in d:
                if d[each] >= start:
                    start = d[each]+1
                    longest = index - start + 1
    #                print('1st',start,longest,ans)
                else:
                    longest += 1
                    ans = max(ans,longest)
                 #   print('2nd',start,longest,ans)

            else:
                longest += 1
                ans = max(ans,longest)
                #print('3rd',start,longest,ans)

            d[each] = index

        return ans
        '''
        ans = 0
        pos = 0 
        longest_len = 0
        d = dict()
        for each in s:
            if each in d:
                if d[each] >= pos - longest_len:
                    d[each] = pos 
                    longest_len = 0
                    pos += 1
                else:
                    d[each] = pos
                    longest_len += 1
                    pos += 1
                    if longest_len > ans:
                        ans = longest_len
                
            else:
                d[each] = pos
                pos += 1
                longest_len += 1
                if longest_len > ans:
                    ans = longest_len
        return ans
        '''
