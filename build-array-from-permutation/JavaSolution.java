// https://leetcode.com/problems/build-array-from-permutation/

class Solution {
    public int[] buildArray(int[] nums) {
        int[] ans = new int[0];
        
        for(int i = 0; i < nums.length; i++) {
            ans = Arrays.copyOf(ans, ans.length + 1);
            ans[ans.length - 1] = nums[nums[i]];
        }
        return ans;
    }
}