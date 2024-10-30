import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());

        int answer = 0;

        Integer[] town = new Integer[n];

        st = new StringTokenizer(br.readLine());

        for (int i=0; i<n; i++) {
            town[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(town);

        int maxNum = town[n-1];

        for (int i=2;i<maxNum+1; i++) {
            int count = 0;
            for (int j=0; j<n; j++) {
                if (town[j] % i == 0) {
                    count += 1;
                }
            }
            if (answer < count) {
                answer = count;
            }
        }
        System.out.println(answer);
    }
}
