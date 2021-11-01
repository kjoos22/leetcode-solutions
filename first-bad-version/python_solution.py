# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

# https://leetcode.com/problems/first-bad-version/

import math

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        first = 1
        last = n
        
        while first < last:
            mid = math.trunc(math.floor(first + ((last - first) / 2)))
            if isBadVersion(mid):
                last = mid
            else:
                first = mid + 1
                
        return first


def isBadVersion(version):
    #pre-defined on leetcode
    return