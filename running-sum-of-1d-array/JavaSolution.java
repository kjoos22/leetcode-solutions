
    // https://leetcode.com/problems/running-sum-of-1d-array/submissions/

class Solution {
    public int[] runningSum(int[] nums) {
        int running_sum = 0;
        int[] running_sums;
        running_sums = new int[nums.length];
            
        for (int i = 0; i < nums.length; i++) {
            running_sum += nums[i];
            running_sums[i] = running_sum;
        }
        return running_sums;
    }
}

