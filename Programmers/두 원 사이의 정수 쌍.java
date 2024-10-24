class Solution {
    public long solution(int r1, int r2) {
        long answer = 0;
        
        long maxCircleH = (long)r2*r2;
        long minCircleH = (long)r1*r1;
        
        
        for (int i=1;i<=r2;i++) {
            long i2 = (long)i*i;
            long maxH = (long)Math.floor(Math.sqrt(maxCircleH - i2));
            long minH = (long)Math.ceil(Math.sqrt(minCircleH - i2));
            answer += maxH - minH + 1;
        }
        return 4*answer;
    }
}