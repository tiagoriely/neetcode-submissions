class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        int n = nums.size();
        unordered_map<int, int> seen;
        seen.reserve(nums.size());
        for (int i = 0; i < n; i++) {
            int diff = target - nums[i];
            auto it = seen.find(diff);
            if (it != seen.end()) {
                return {it->second, i};
            }

            seen.insert({nums[i], i});

        }
        return {};
    }
};
