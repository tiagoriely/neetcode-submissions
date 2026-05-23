class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        /* 
         * Iteration: two passes
         * Time: O(n)
         * Space: O(n)
         */
        vector<int> ans;

        for (int i = 0; i < 2; i++) {
            for (int num: nums) {
                ans.push_back(num);
            }
        }

        return ans;
    }
};