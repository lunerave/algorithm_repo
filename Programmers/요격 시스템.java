import java.util.*;

class Solution {
    public int solution(int[][] targets) {
        int answer = 0;
        
        Arrays.sort(targets, (o1, o2) -> o1[1] == o2[1] ? o1[0] - o2[0] : o1[1] - o2[1]);
        
        int e = 0;
        
        for (int[] tar : targets) {
            if (tar[0] >= e) {
                answer++;
                e = tar[1];
            }
        }
        
        return answer;
    }
}