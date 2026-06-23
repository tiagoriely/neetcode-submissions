class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded_string;

        for (const string& s: strs) {
            encoded_string.append(to_string(s.size()));
            encoded_string.push_back('#');
            encoded_string.append(s);
        }
        cout << encoded_string;
        return encoded_string;
        
    }

    vector<string> decode(string s) {

        vector<string> decoded_strs;

        int i = 0;
        while (i < s.size()) {

            // find #
            int j = i;
            while (s[j] != '#')
                j++;
            
            // find string length  
            int length = stoi(s.substr(i, j - i));

            // Find start of the word
            i = j + 1;
            
            decoded_strs.push_back(s.substr(i, length));

            // set i to next word size
            i += length;
        }
        
        return decoded_strs;
    }
};
