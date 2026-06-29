class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());

        // initialise the longest sequence
        int longest = 0;

        // Range-based loop through the set
        for (int num: numSet) {

            // Find a value that is the smallest of the sequence
            if (numSet.find(num - 1) == numSet.end()) {
                int length = 0;
                // extend the sequence as long as the next number exists
                while (numSet.find(num + length) != numSet.end()) {
                    length++;
                }
                longest = max(longest, length);
            }
        }
        return longest;
    }
};
