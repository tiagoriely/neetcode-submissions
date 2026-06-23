class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int total_product{1};
        int total_product_non_zero {1};
        int zero_count {0};
        for (const int& val: nums) {
            if (zero_count == 2)
                break;
            if (val == 0)
                zero_count++;
            if (val != 0)
                total_product_non_zero *= val;
            
            total_product *= val;
        }

        vector<int> output;
        for (const int& val: nums) {
            if (val != 0) 
                output.push_back(total_product / val);
            else if (zero_count < 2)
                output.push_back(total_product_non_zero);
            else
                output.push_back(0);
        }
        cout << total_product;
        return output;
    }
};
