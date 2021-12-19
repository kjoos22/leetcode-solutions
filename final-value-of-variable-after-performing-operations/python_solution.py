# https://leetcode.com/problems/final-value-of-variable-after-performing-operations

class Solution:
    def finalValueAfterOperations(self, operations):
        value = 0
        for op in operations:
            if "+" in op:
                value += 1
            else:
                value -= 1
        return value