import java.util.*;

class Solution {
    public int solution(int n, int[] stations, int w) {
        int answer = 0;
        
        // 전파 범위
        int wifi = w*2+1;
        
        // 첫 번째 아파트부터 시작
        int start = 1;
        
        int end;
        
        int check;
        
        for (int i=0;i<stations.length;i++) {
            // 기지국에서 전파 끝 범위
            end = stations[i] - w;
            // 이전에 전파범위가 안닿는 시작 범위가 기지국에서 닿는 지 확인
            if (end - start <= 0) {
                start = stations[i]+w+1;
                continue;
            }
            // 안 닿고 있는 아파트 부분이 있음
            check = end-start;
            
            // 안 닿는 부분 기지국 설치
            answer += check/wifi;
            if (check%wifi != 0) {
                answer += 1;
            }
            // 안 닿는 시작 부분 초기화
            start = stations[i]+w+1;
        }
        
        // 기지국 기준 탐색이 끝난 후, 나머지 부분이 있는 지 확인
        if (start <= n) {
            check = n+1-start;
            answer += check/wifi;
            if (check%wifi != 0) {
                answer += 1;
            }
        }
        return answer;
    }
}