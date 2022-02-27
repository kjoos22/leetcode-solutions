# @param {String} jewels
# @param {String} stones
# @return {Integer}

# https://leetcode.com/problems/jewels-and-stones/

def num_jewels_in_stones(jewels, stones)
    jewels = jewels.split("")
    total_jewels = 0
    
    for jewel in jewels
         total_jewels += stones.count(jewel)
    end
    
    total_jewels
end