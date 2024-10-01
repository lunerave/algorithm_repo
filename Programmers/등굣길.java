import java.util.*;

class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int answer = 0;
        
        int[][] dp = new int[n][m];
        
        // 첫 번째 열 최단 경로 개수 초기화
        for (int i=1;i<m;i++) {
            // 진행 중 웅덩이 만나면 더 이상 경로 없음
            if (check(0, i, puddles)) {
                dp[0][i] = 0;
                break;
            } else {
                dp[0][i] = 1;
            }
        }
        
        // 첫 번째 행 경로 개수 초기화
        for (int i=1;i<n;i++) {
            // 진행 중 웅덩이 만나면 더 이상 경로 없음
            if (check(i, 0, puddles)) {
                dp[i][0] = 0;
                break;
            } else {
                dp[i][0] = 1;

            }
        }
        
        for (int i=1;i<n;i++) {
            for (int j=1;j<m;j++) {
                // 현재 경로가 웅덩이인지 확인, 웅덩이라면 경로 불가
                if (check(i, j, puddles)) {
                    dp[i][j] = 0;
                } else {
                    // 위에서 아래로, 왼쪽에서 오른쪽으로만 경로가 가능
                    dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007;
                }
            }
        }
                
        return dp[n-1][m-1];
    }
    
    public boolean check(int x, int y, int[][] puddles) {
        for (int i=0;i<puddles.length;i++) {
            int[] temp = puddles[i];
            
            if (y == temp[0]-1 && x == temp[1]-1) {
                return true;
            }
        }
        return false;
    }
}