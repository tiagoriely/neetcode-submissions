class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // If empty return 0
        if (nums.empty())
            return 0;
        
        // Sort vector (increasing order)
        sort(nums.begin(), nums.end());

        int res{0}, curr{nums[0]}, length = 0;

        int i = 0;
        while (i < nums.size()) {
            if (curr != nums[i]) {
                curr = nums[i];
                length = 0;
            }
            
            // skip is same values
            while (i < nums.size() && curr == nums[i]) {
                i++;
            }
            length++;
            curr++;
            res = max(res, length);
        }
        return res;
    }
};
