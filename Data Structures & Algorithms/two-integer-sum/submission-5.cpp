class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        /* Brute force
         *
         * Time: O(n^2)
         * Space: O(1)
         */

        int n = nums.size();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                
                if (i != j && nums[i] + nums[j] == target)
                    return {i, j};
            }
        }

        return {};
    }
};
