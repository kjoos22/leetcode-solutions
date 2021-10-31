#https://leetcode.com/problems/binary-search
def search(nums, target)
    if nums.last < target
        return -1
    end
    
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
    return -1
end