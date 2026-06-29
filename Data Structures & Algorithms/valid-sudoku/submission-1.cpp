class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map <int, unordered_set<char>> rowCheck;
        unordered_map <int, unordered_set<char>> columnCheck;
        map<pair<int, int>, unordered_set<char>> gridCheck;

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {

                if (board[r][c] == '.')
                    continue;

                if (rowCheck[r].count(board[r][c]))
                    return false;
                if (columnCheck[c].count(board[r][c]))
                    return false;
                
                pair <int, int> squareKey = {r / 3, c / 3};
                if (gridCheck[squareKey].count(board[r][c]))
                    return false;
                
                rowCheck[r].insert(board[r][c]);
                columnCheck[c].insert(board[r][c]);
                gridCheck[squareKey].insert(board[r][c]);
            }

            
        }
        return true;
    }
};
