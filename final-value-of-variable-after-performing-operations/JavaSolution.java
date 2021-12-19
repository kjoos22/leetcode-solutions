// https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int value = 0;
            for(int i = 0; i < operations.length; i++) {
                if (operations[i].contains("+")) {
                    value += 1;
                }else {
                    value -= 1;
                }
            }
        return value;
    }
}