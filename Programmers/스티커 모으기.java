import java.util.*;

class Solution {
    public int solution(int sticker[]) {
        int answer = 0;
        
        // 스티커 길이가 1이라면 그 스티커만 뜯어낸다
        if (sticker.length == 1) {
            return sticker[0];
        }
        
        // 첫 번째 스티커를 뗀 경우 탐색
        int[] dpF = new int[sticker.length];
        
        dpF[0] = sticker[0];
        
        dpF[1] = dpF[0];
        
        // 두 번째 스티커를 뗀 경우 탐색
        int[] dpS = new int[sticker.length];
        
        dpS[0] = 0;
        
        dpS[1] = sticker[1];
        
        // 첫 번째 스티커를 뗀 경우, 마지막 스티커는 뗄 수 없다.
        for (int i=2;i<sticker.length;i++) {
            if (i==sticker.length-1) {
                dpF[i] = Math.max(dpF[i-2], dpF[i-1]);
            } else {
                dpF[i] = Math.max(dpF[i-2] + sticker[i], dpF[i-1]);
            }
        }
        
        // 두 번째 스티커를 뗀 경우, 마지막 스티커 떼는 것이 가능하다.
        for (int i=2;i<sticker.length;i++) {
            dpS[i] = Math.max(dpS[i-1], dpS[i-2] + sticker[i]);
        }
        
        // 두 경우에서 마지막 값이 가장 큰 것을 리턴한다.
        return Math.max(dpS[sticker.length-1], dpF[sticker.length-1]);
    }
}