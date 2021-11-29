# @param {Integer[]} nums
# @return {Integer[]}

# https://leetcode.com/problems/concatenation-of-array

def get_concatenation(nums)
    ans = []
    
    for num in nums do
       ans.push(num) 
    end
    for num in nums do
       ans.push(num) 
    end
    
    return ans
end