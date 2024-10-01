import java.util.*;

class Solution {
    public int solution(int[] A, int[] B) {
        int answer = 0;
        
        // min heap을 구현해서 B 숫자가 A 숫자의 작은 숫자부터 해결하도록 구현
        PriorityQueue<Integer> pqA = new PriorityQueue<>();
        PriorityQueue<Integer> pqB = new PriorityQueue<>();
        
        for (int i=0;i<A.length;i++) {
            pqA.offer(A[i]);
            pqB.offer(B[i]);
        }
        
        while (!pqB.isEmpty()) {
            int n = pqB.poll();
            
            // 현재 A숫자의 가장 작은 숫자를 B가 가진 가장 작은 숫자로 해결 가능한지 탐색
            if (pqA.peek() < n) {
                answer += 1;
                pqA.poll();
            }
        }
        
        return answer;
    }
}