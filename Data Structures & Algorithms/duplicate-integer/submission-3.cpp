class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        /*
         * Hash Set: unordered_map
         *  time: O(n^2)
         *  space: O(1)
         */
        unordered_set<int> seen;
        for (auto num: nums) {
            if (seen.count(num)) {
                return true;
            }
            seen.insert(num);
        }
        return false;
    }
};