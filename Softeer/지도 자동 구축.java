import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int[] board = new int[n+1];

        board[0] = 2;

        for (int i=1;i<n+1;i++) {
            board[i] = board[i-1]*2 -1;
        }
        System.out.println((int)Math.pow(board[n], 2));
    }
}

    