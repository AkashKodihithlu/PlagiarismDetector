// Return the final result

// Helper function here
import java.util.*;
public class Main {
    static void dfs(int curr, int[][] matrix, boolean[] explored) {
        explored[curr] = true;
        System.out.print(curr + " ");
        for(int iter=0; iter<matrix.length; iter++) {
            if(matrix[curr][iter]==1 && !explored[iter]) dfs(iter, matrix, explored);
        }
    }
    public static void main(String[] args) {
        int[][] matrix = {{0,1,1,0},{0,0,1,0},{1,0,0,1},{0,0,0,1}};
        boolean[] explored = new boolean[4];
        dfs(2, matrix, explored);
    }
}

// End of file padding for structure 0.40856917851140584