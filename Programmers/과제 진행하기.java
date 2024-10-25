import java.util.*;

class Solution {
    public List<String> solution(String[][] plans) {
        List<String> answer = new ArrayList<>();
        int answerIdx = 0;
        Plan[] ps = new Plan[plans.length] ;
        for(int i=0;i<plans.length;i++) {
            ps[i] = new Plan(plans[i][0], plans[i][1], plans[i][2]);
        }
        Arrays.sort(ps, (o1, o2) -> o1.start - o2.start);
        
        Stack<Plan> stack = new Stack<>();
        
        for (int i=0;i<plans.length - 1;i++) {
            Plan curPlan = ps[i];
            Plan nextPlan = ps[i+1];
            
            if (curPlan.getEndTime() > nextPlan.start) {
                curPlan.playtime = curPlan.getEndTime() - nextPlan.start;
                stack.push(curPlan);
                continue;
            }
            
            answer.add(curPlan.name);
            
            int restTime = nextPlan.start - curPlan.getEndTime();
            
            while (restTime > 0 && !stack.isEmpty()) {
                Plan stackPlan = stack.peek();
                if (restTime < stackPlan.playtime) {
                    stackPlan.playtime -= restTime;
                    break;
                } else {
                    restTime = restTime - stackPlan.playtime;
                    answer.add(stack.pop().name);
                }
            }
        }
        
        answer.add(ps[plans.length-1].name);
        
        while (!stack.isEmpty()) {
            answer.add(stack.pop().name);
        }
        
        return answer;
    }
}

class Plan {
    String name;
    int start;
    int playtime;
    
    public Plan(String name, String start, String playtime) {
        this.name = name;
        String[] time = start.split(":");
        this.start = Integer.parseInt(time[0]) * 60 + Integer.parseInt(time[1]);
        this.playtime = Integer.parseInt(playtime);
    }
    
    public int getEndTime() {
        return start + playtime;
    }
    
    
}