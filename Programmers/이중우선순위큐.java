import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        int[] answer = {};
        
        // max heap과 min heap을 함께 사용할여 문제 해결
        PriorityQueue<Integer> maxPQ = new PriorityQueue<>((i1, i2) -> i2 - i1);
        PriorityQueue<Integer> minPQ = new PriorityQueue<>();
        
        for (int i=0;i<operations.length;i++) {
            String[] commands = operations[i].split(" ");
            if (commands[0].equals("I")) {
                maxPQ.offer(Integer.parseInt(commands[1]));
                minPQ.offer(Integer.parseInt(commands[1]));
            } else { // command가 "D"로 들어왔을 때
                // heap이 비어있을 때는 무시한다, 1일 때는 최댓값 삭제
                if (commands[1].equals("1") && !maxPQ.isEmpty()) {
                    minPQ.remove(maxPQ.poll());
                // heap이 비어있을 때는 무시한다, 0일 때는 최솟값 삭제    
                } else if (commands[1].equals("-1") && !minPQ.isEmpty()){
                    maxPQ.remove(minPQ.poll());
                }
            }
        }
        
        int max = 0;
        int min = 0;
        
        if (!minPQ.isEmpty()) {
            max = maxPQ.poll();
            min = minPQ.poll();
        }
            
        return new int[]{max, min};
    }
}