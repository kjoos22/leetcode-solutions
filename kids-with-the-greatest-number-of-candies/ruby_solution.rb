# @param {Integer[]} candies
# @param {Integer} extra_candies
# @return {Boolean[]}

# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

def kids_with_candies(candies, extra_candies)
    most_candies = candies.max
    have_most_candies = []
    for candy in candies
        if candy + extra_candies >= most_candies
            have_most_candies.push(true)
        else
            have_most_candies.push(false)
        end
    end
    return have_most_candies
end