# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 16:24:38 2019

@author: naveenpc
"""

def longest_substring(s):
    start = 0
    longest = 0
    ans = 0 
    d = dict()
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


print(longest_substring('aab'))
assert(longest_substring('aab')==2)
assert(longest_substring('avdk')==4)
assert(longest_substring('dvdk') ==3)
assert(longest_substring('bbbbbb') == 1)
assert(longest_substring('abcdeabcdef')==6)
assert(longest_substring('abcdefghijkl')==12)