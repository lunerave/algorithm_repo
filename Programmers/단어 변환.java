import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        
        int t = -1;
        
        // target 단어의 index 저장
        for (int i=0;i<words.length;i++) {
            if (target.equals(words[i])) {
                t = i;
                break;
            }
        }
        
        // t가 -1이라면 words내에 target이 없다
        if (t == -1) {
            return 0;
        }
        
        Queue<Node> q = new LinkedList<>();
        
        int INF = Integer.MAX_VALUE;
        
        // 거리 비교를 통해, 가장 최솟값으로 변환 가능한지 확인
        int[] distance = new int[words.length];
        
        Arrays.fill(distance, INF);
        
        q.offer(new Node(begin, 0));
        
        while (!q.isEmpty()) {
            Node nd = q.poll();
            
            // 전체 단어를 탐색한다
            for (int i=0;i<words.length;i++) {
                // 현재 단어와 탐색 단어 비교
                if (compare(nd.name, words[i])) {
                    int nc = nd.count + 1;
                    
                    // 거리가 짧은 것만 더 탐색하면 된다
                    if (distance[i] > nc) {
                        distance[i] = nc;
                        q.offer(new Node(words[i], nc));
                    }
                        
                }
            }
        }
        
        if (distance[t] == INF) {
            return 0;
        }
        
        return distance[t];
    }
    
    // 문자열 비교 함수
    public boolean compare(String a, String b) {
        int sLen = a.length();
        
        int c = 0;
        
        for (int j=0;j<sLen;j++) {
            char tempA = a.charAt(j);
            char tempB = b.charAt(j);
            
            if (tempA != tempB) {
                c++;
            }
            
            // 다른거 2개 이상이라면 조건을 벗어난다
            if (c>=2) {
                return false;
            }
        }
        
        return true;
    }
    
    // Queue에 들어갈 구조체 설정
    class Node {
        String name;
        int count;
        
        public Node(String name, int count) {
            this.name = name;
            this.count = count;
        }
    }
}