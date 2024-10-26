import java.util.*;

class Solution {
    static int length;
    static int[] visited;
    static String[][] sTickets;
    static ArrayList<String> cands = new ArrayList<>();
    
    public String[] solution(String[][] tickets) {
        String[] answer = {};
        
        length = tickets.length;
        
        visited = new int[length];
        
        sTickets = tickets;
        
        dfs("ICN", "ICN", 0);
        
        Collections.sort(cands);
        
        return cands.get(0).split(" ");
    }
    
    void dfs(String start, String route, int depth) {
        if (depth == length) {
            cands.add(route);
            return;
        }
        
        for (int i=0;i<length;i++) {
            if (visited[i] == 0 && start.equals(sTickets[i][0])) {
                visited[i] = 1;
                dfs(sTickets[i][1], route + " " + sTickets[i][1], depth + 1);
                visited[i] = 0;
            }
        }
    }
}