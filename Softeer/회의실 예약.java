import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int room = Integer.parseInt(st.nextToken());
        int info = Integer.parseInt(st.nextToken());

        Map<String, int[]> dic = new HashMap<>();
        
        for (int i=0;i<room;i++) {
            st = new StringTokenizer(br.readLine());
            dic.put(st.nextToken(), new int[19]);
        }

        for (int i=0;i<info;i++) {
            st = new StringTokenizer(br.readLine());
            String roomName = st.nextToken();
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());

            int[] times = dic.get(roomName);
            
            for (int t=start;t<end;t++) {
                times[t] = 1;
            }
        }

        List<String> keys = new ArrayList<>(dic.keySet());
        Collections.sort(keys);

        for (int i=0;i<room;i++) {
            System.out.println("Room " + keys.get(i) + ":");
            int[] times = dic.get(keys.get(i));
            List<int []> proom = new ArrayList<>(); 
            int startFlag = 0;
            int start = 0;
            int end = 0;
            for (int t=9;t<19;t++) {
                if (times[t] == 0 && startFlag == 1 && t==18) {
                    proom.add(new int[]{start, 18});
                }
                if (times[t] == 0 && startFlag == 0) {
                    startFlag = 1;
                    start = t;
                } 
                if (times[t] == 1 && startFlag == 1) {
                    startFlag = 0;
                    end = t;
                    proom.add(new int[]{start, end});
                }
            }
            if (proom.size() == 0) {
                System.out.println("Not available");
            } else {
                System.out.println(proom.size() + " available:");
                for (int[] a: proom) {
                    System.out.println(String.format("%02d-%02d", a[0], a[1]));
                }
            }
            if (i != keys.size()-1) {
                System.out.println("-----");
            }
        }
        
    }
}
