class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0, right = s.length() - 1;

        while (left < right) {
            cout << endl << endl << "ENTERING: " 
                 << s[left] << " and " << s[right] << endl;
            while (left < right && !isalnum(s[left])) {
                cout << "left incremented: " << s[left] << endl;
                left++;
            }

            while (left < right && !isalnum(s[right])) {
                cout << "right incremented: " << s[right] << endl; 
                right--;
            }

            if (tolower(s[left]) == tolower(s[right])) {
                        cout << s[left] << " and " << s[right] << endl;
                        left++;
                        right--;
                    }
            
            else {
                return false;
            }
        }
        return true;
    }
};
