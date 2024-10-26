import java.util.*;

class Solution {
    String[] userIds;
    String[] bannedIds;
    HashSet<HashSet<String>> result = new HashSet<>();
    public int solution(String[] user_id, String[] banned_id) {
        int answer = 0;
                
        userIds = user_id;
        bannedIds = banned_id;
                
        dfs(new HashSet<>(), 0);
        
        return result.size();
    }
    
    void dfs(HashSet<String> set, int depth) {
        if (depth == bannedIds.length) {
            result.add(set);
            return;
        }
        
        for (int i=0; i< userIds.length; i++) {
            if (set.contains(userIds[i])) {
                continue;
            }
            
            if (check(userIds[i], bannedIds[depth])) {
                set.add(userIds[i]);
                dfs(new HashSet<>(set), depth + 1);
                set.remove(userIds[i]);
            }
        }
    }
    
    boolean check(String userId, String bannedId) {
        if (userId.length() != bannedId.length()) {
            return false;
        }
        
        int flag = 1;
        
        for (int i=0;i<userId.length();i++) {
            if (bannedId.charAt(i) != '*' && userId.charAt(i) != bannedId.charAt(i)) {
                flag = 0;
                break;
            }
        }
        
        if (flag == 0) {
            return false;
        }
        
        return true;
    }
}