# @param {String[]} operations
# @return {Integer}

# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

def final_value_after_operations(operations)
    value = 0
    operations.each do |op|
        op = op.split("")
        if op.include?("+")
            value += 1
        else
            value -= 1
        end
    end
    value   
end