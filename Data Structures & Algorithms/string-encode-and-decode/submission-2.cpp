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
            // Find '#'
            int j = i;
            while (s[j] != '#')
                j++;
            
            // Find size of word
            int length = stoi(s.substr(i, j - i));
            // Point to the first letter of the word
            i = j + 1;

            decoded_strs.push_back(s.substr(i, length));

            i += length;

        }
        return decoded_strs;
    }
};
