import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int[][] land = new int[3][3];
        int answer = 100;

        for (int i=0;i<3;i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0;j<3;j++) {
                land[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        for (int i=0;i<3;i++) {
            int[] temp = Arrays.copyOf(land[i], 3);
            Arrays.sort(temp);
            int cost = 0;
            for (int j=0;j<2;j++) {
                cost += temp[j+1] - temp[j];
            }
            if (answer > cost) {
                answer = cost;
            }
        }
        for (int i=0;i<3;i++) {
            int[] temp = new int[3];
            temp[0] = land[0][i];
            temp[1] = land[1][i];
            temp[2] = land[2][i];
            Arrays.sort(temp);
            int cost = 0;
            for (int j=0;j<2;j++) {
                cost += temp[j+1] - temp[j];
            }
            if (answer > cost) {
                answer = cost;
            }
        }
        System.out.println(answer);
    }
}
