import java.util.Arrays;

//https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        
        int mostCandies = Arrays.stream(candies).max().getAsInt();
        List<Boolean> haveMostCandies = new ArrayList<Boolean>();
        
        for (int i = 0; i < candies.length; i++) {
            if (candies[i] + extraCandies >= mostCandies) {
                haveMostCandies.add(true);
            } else {
                haveMostCandies.add(false);
            }
        }
        return haveMostCandies;
    }
}