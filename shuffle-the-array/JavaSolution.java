// https://leetcode.com/problems/shuffle-the-array

class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] shuffled_nums = new int[n * 2];
        int x = 0;
        for (int i = 0; i < n; i++) {
            shuffled_nums[x] = nums[i];
            shuffled_nums[x + 1] = nums[i + n];
            x = x + 2;
        }
        return shuffled_nums;
    }
}