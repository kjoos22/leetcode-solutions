/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

// https://leetcode.com/problems/first-bad-version/

import java.lang.Math;

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int first = 1;
        int last = n;
        
        while (first < last) {
            int mid = (int) Math.floor((first + (last - first) / 2));
            if (isBadVersion(mid)){
                last = mid;
            } else {
                first = mid + 1;
            }
        }
        
        return first;
    }
}