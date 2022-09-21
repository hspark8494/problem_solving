package programmers;

// Q1829 카카오프렌즈 컬러링북
// https://school.programmers.co.kr/learn/courses/30/lessons/1829?language=java
import java.util.Arrays;
import java.util.concurrent.atomic.AtomicInteger;

class Solution {
	boolean[][] visited;
	int[][] picture;
	int maxSizeOfOneArea = 0;
	
    public int[] solution(int m, int n, int[][] picture) {
    	visited = new boolean[m][n];
    	this.picture = picture;
    	int numberOfArea = 0;
    	
    	for(int i=0; i<picture.length; i++) {
    		for(int j=0; j<picture[0].length; j++) {
    			if(picture[i][j] != 0 && !visited[i][j]) {
    				numberOfArea++;
    				AtomicInteger ai = new AtomicInteger(0);
    				dfs(i,j,ai);
    			}
    		}
    	}
    	
        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
    
    AtomicInteger dfs(int m, int n, AtomicInteger count) {
    	visited[m][n] = true;
    	maxSizeOfOneArea = Math.max(maxSizeOfOneArea, count.addAndGet(1));
    	//DOWN
    	if(check(m-1, n, picture[m][n])) {
    		dfs(m-1, n, count);
    	}
    	//UP
    	if(check(m+1, n, picture[m][n])) {
    		dfs(m+1, n, count);
    	}
    	//LEFT
    	if(check(m, n-1, picture[m][n])) {
    		dfs(m, n-1, count);
    	}
    	//RIGHT
    	if(check(m, n+1, picture[m][n])) {
    		dfs(m, n+1, count);
    	}
    	return count;
    }
    
    boolean check(int m, int n, int color) {
    	return m>=0 && m<picture.length && n>=0 && n<picture[0].length && !visited[m][n] && picture[m][n] == color;
    }

    public static void main(String[] args) {
		Solution sol = new Solution();
		int[][] arr = {{1, 1, 1, 0}, {1, 2, 2, 0}, {1, 0, 0, 1}, {0, 0, 0, 1}, {0, 0, 0, 3}, {0, 0, 0, 3}};
		int[] result = sol.solution(6, 4, arr);
		
		System.out.println(Arrays.toString(result));
	}
}