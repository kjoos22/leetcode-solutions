# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        most_candies = max(candies)
        have_most_candies = []
        for candy in candies:
            if candy + extraCandies >= most_candies:
                have_most_candies.append(True)
            else:
                have_most_candies.append(False)
        return have_most_candies