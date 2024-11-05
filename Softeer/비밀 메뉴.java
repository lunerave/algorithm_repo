import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        int[] secret = new int[m];
        
        for (int i=0;i<m;i++) {
            secret[i] = Integer.parseInt(st.nextToken());
        }

        int[] click = new int[n];

        st = new StringTokenizer(br.readLine());
        
        for (int i=0;i<n;i++) {
            click[i] = Integer.parseInt(st.nextToken());
        }

        // System.out.println(q.peek());

        int secretIdx = 0;
        int flag = 1;
        
        for (int i=0;i<n;i++) {
            if (flag == 0) {
                break;
            }
            for (int j=i;j<n;j++) {
                if (click[j] == secret[secretIdx]) {
                    if (secretIdx == (m-1)) {
                        System.out.println("secret");
                        flag = 0;
                        break;
                    }
                    secretIdx += 1;
                } else {
                    secretIdx = 0;
                }
            }
        }
        if (flag != 0) {
            System.out.println("normal");
        }
    }
}
