public class IslandPerimeter {
    public int islandPerimeter(int[][] grid) {
        int perimeter = 0;
        int m = grid.length;
        int n = grid[0].length;
        if (grid == null || m == 0 || n == 0) 
            return perimeter;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    perimeter = perimeter + 4;;
                    if (i > 0 && grid[i-1][j] == 1)
                        perimeter = perimeter - 2;
                    if (j > 0 && grid[i][j-1] == 1)
                        perimeter = perimeter - 2;
                }
            }
        }
        return perimeter;
    }
}