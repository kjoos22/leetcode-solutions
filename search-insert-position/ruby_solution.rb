# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
# https://leetcode.com/problems/search-insert-position/submissions/
def search_insert(nums, target)
    start = 0
    last = nums.length - 1
    
    while start <= last
        mid = ((start + last) / 2).floor
        
        if nums[mid] == target
            return mid
        end
        
        if target < nums[mid]
            last = mid - 1
        else
            start = mid + 1
        end        
    end
    
    for i in nums do
        if i > target
            return nums.find_index(i)
        end
        if nums.find_index(i) == nums.length - 1
            return nums.find_index(i)+1
        end
    end
end