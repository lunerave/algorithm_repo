import java.util.*;

class Solution {
    public long solution(int n, int[] works) {
        long answer = 0;
        
        // 타입이 Long일 경우, 비교하는 메소드를 따로 적용해야한다.
        PriorityQueue<Long> pq = new PriorityQueue<>((i1, i2) -> Long.compare(i2, i1));
        
        for (int i=0;i<works.length;i++) {
            pq.offer((long)works[i]);
        }
        
        while (!pq.isEmpty() && n > 0) {
            long work = pq.poll();
            // work가 0이라면, 이미 모든 일 처리 완료
            if (work == 0) {
                break;
            }
            work -= 1;
            n -= 1;
            pq.offer(work);
        }
        
        // 일이 남아있다면 야근 피로도 계산
        while (!pq.isEmpty()) {
            long temp = pq.poll();
            answer += temp*temp;
        }
        
        return answer;
    }
}