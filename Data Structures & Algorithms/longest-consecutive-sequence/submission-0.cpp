#include <algorithm>

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

        int n = nums.size();
        int left = 0;
        int right = 0; 

             
        
        if (n == 0)
            return 0;

        sort(nums.begin(), nums.end());

        int count = 1;
        while (left < n) {
            vector<int> sequence {nums[left]};
            while (right < n) {
                if (nums[right] == sequence[sequence.size() - 1] + 1)
                    sequence.push_back(nums[right]);
                right++;
            }
            int length = sequence.size();
            cout << length << endl;
            count = max(count, length);
            
            left++;
            right = left;
        }

        return count;
    }

};
