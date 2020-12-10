class Solution {
private:
    void dfs(vector<vector<char>>& grid, int r, int c) {
        if (r < 0 || r > grid.size() - 1) {
            return;
        }
        
        if (c < 0 || c > grid[0].size()- 1) {
            return;
        }
        
        if (grid[r][c] == '0') {
            return;
        }
        
        grid[r][c] = '0';
        
        dfs(grid, r - 1, c);
        dfs(grid, r + 1, c);
        dfs(grid, r, c - 1);
        dfs(grid, r, c + 1);
    }
public:
    int numIslands(vector<vector<char>>& grid) {
        int r = grid.size();
        if (!r) {
            return 0;
        }
        int answer = 0;
        int c = grid[0].size();
        for (int i = 0; i< r; ++i) {
            for (int j=0; j< c; ++j) {
                if (grid[i][j] == '1')
                answer ++;
                dfs(grid, i, j);
            }
        }
        return answer;
    }
};
