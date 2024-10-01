import java.util.*;

class Solution {
    public int[] solution(int n, int s) {
        
        // 곱한 값이 최대가 되려면 평균이 비슷할 수록 큼
        int div = s/n;
        int mod = s%n;
        
        // 3가지 숫자의 합으로 만드는 것이 불가능
        if (div == 0) {
            return new int[]{-1};
        }
        
        int[] answer = new int[n];
        
        // 평균값으로 초기화
        for (int i=0;i<n;i++) {
            answer[i] = div;
        }
        
        // 오름차순 정렬을 위해 뒤 인덱스부터 값 증가
        int index = n-1;
        
        while (mod != 0) {
            mod -= 1;
            answer[index] += 1;
            index -= 1;
        }
        
        return answer;
    }
}