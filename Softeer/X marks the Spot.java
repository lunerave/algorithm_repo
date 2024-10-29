import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());

        StringBuilder sb = new StringBuilder();

        for (int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            String S = st.nextToken().toUpperCase();
            String T = st.nextToken().toUpperCase();

            int xPos = S.indexOf("X");
            sb.append(T.charAt(xPos));
        }
        System.out.println(sb);
    }
}
