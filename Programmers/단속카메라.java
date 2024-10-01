import java.util.*;

class Solution {
    public int solution(int[][] routes) {
        int answer = 0;
        
        // 두 번째 인자를 오름차순으로 정렬한다.
        Arrays.sort(routes, (i1, i2) -> (i1[1] == i2[1] ? i1[0] - i2[0] : i1[1] - i2[1]));
        
        answer += 1;
        // 첫 번째 cctv를 첫 번째 차량의 진출 지점에 설치한다.
        int cctv = routes[0][1];
        
        // 현재 마지막 cctv의 위치와 다음 차량의 진입시점을 비교해서
        // cctv가 다음 차량의 진입 시점을 못 찍고 있다면 추가해야한다
        for (int i=1;i<routes.length;i++) {
            if (cctv < routes[i][0]) {
                answer += 1;
                cctv = routes[i][1];
            }
        }
        return answer;
    }
}