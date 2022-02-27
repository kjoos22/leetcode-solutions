# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total_jewels = 0
        
        for jewel in jewels:
            total_jewels += stones.count(jewel)
            
        return total_jewels