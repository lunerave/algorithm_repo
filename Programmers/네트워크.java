import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        
        // 방문 경로 저장
        int[] visited = new int[n];
        
        for (int i=0;i<n;i++) {
            // 현재 노드를 방문하지 않았다면 탐색 => 새로운 네트워크 발견
            if (visited[i] == 0) {
                Queue<Integer> q = new LinkedList<>();
                
                q.offer(i);
                
                visited[i] = 1;
                
                // 연결된 노드 탐색
                while (!q.isEmpty()) {
                    int now = q.poll();
                    
                    for (int j=0;j<n;j++) {
                        if (j != now && visited[j] == 0 && computers[now][j] == 1) {
                            visited[j] = 1;
                            q.offer(j);
                        }
                    }
                }
                answer += 1;
            }
        }
        return answer;
    }
}