// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

// https://leetcode.com/problems/first-bad-version/

class Solution {
public:
    int firstBadVersion(int n) {
        int first = 1, last = n;
        
        while (first < last)  {
            int mid = first + (last - first) / 2;
            if (isBadVersion(mid)){
                last = mid;
            } else {
                first = mid + 1;
            }
        }
        return first;
    }
};