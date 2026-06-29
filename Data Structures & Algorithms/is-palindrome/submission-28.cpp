class Solution {
public:
    bool isPalindrome(string s) {
        int n = s.size();
        int left{0}, right{n - 1};

        while (left < right && left < n) {
            while (left < right && (ispunct(s[left]) || isspace(s[left])))
                left++;
            while (right > left && (ispunct(s[right]) || isspace(s[right])))
                right--;
            
            if (tolower(s[left]) != tolower(s[right]))
                return false;
            left++;
            right--;
        }

        return true;
    }
};
