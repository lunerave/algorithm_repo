import java.util.*;

class Solution {
    public int solution(int[][] triangle) {
        int answer = 0;
        
        int tLen = triangle.length;
        
        // dp 초기화
        int[][] dp = new int[tLen][tLen];
        dp[0][0] = triangle[0][0];
        
        // 두 번째 줄부터 탐색 시작, 같은 줄 위의 노드와 같은 줄 위 왼쪽 노드만 탐색하면 된다.
        for (int i=1;i<tLen;i++) {
            // 트라이앵글식으로 저장된 노드들 순회하며 탐색
            for (int j=0;j<i+1;j++){
                // j가 0일 때는, 왼쪽 노드 탐색 불가
                if (j == 0) {
                    dp[i][j] = dp[i-1][j] + triangle[i][j];
                    answer = Math.max(answer, dp[i][j]);
                } else {
                    dp[i][j] = Math.max(dp[i-1][j-1] + triangle[i][j], dp[i-1][j] + triangle[i][j]);
                    answer = Math.max(answer, dp[i][j]);
                }
            }
        }
        
        return answer;
    }
}