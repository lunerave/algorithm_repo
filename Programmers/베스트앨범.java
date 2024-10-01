import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        // 정답을 저장하기 위한 임시 리스트
        ArrayList<Integer> tempAnswer = new ArrayList<>();
        
        HashMap<String, Integer> dict = new HashMap<>();
        
        // hash에 저장되어있는 키인지 확인하기 위한 flag
        int dictFlag = 0;
        
        for (int i=0;i<genres.length;i++) {
            // key가 이미 hash에 저장되어 있다면, 재생횟수 추가
            for (String temp: dict.keySet()) {
                if (temp.equals(genres[i])) {
                    dict.put(genres[i], dict.get(genres[i]) + plays[i]);
                    dictFlag = 1;
                    break;
                }
            }
            if (dictFlag == 1) {
                dictFlag = 0;
                continue;
            } else { //key가 저장되어 있지 않았다면, key와 값 추가
                dict.put(genres[i], plays[i]);
            }
        }
        
        // key의 value를 기준으로 내림차순 정렬1
        List<String> keySet = new ArrayList<>(dict.keySet());
        // key의 value를 기준으로 내림차순 정렬2
        keySet.sort((i1, i2) -> (dict.get(i2).compareTo(dict.get(i1))));
        
        // 최대 2개만 추가
        int count;
        
        for (String key: keySet) {
            // 장르의 재생횟수 임시 저장
            ArrayList<int[]> temp = new ArrayList<>();
            for (int i=0;i<genres.length;i++) {
                if (key.equals(genres[i])) {
                    temp.add(new int[]{plays[i], i});
                }
            }
            // 재생횟수 기준 먼저 내림차순 정렬, 같다면 고유번호 기준 오름차순 정렬
            temp.sort((i1, i2) -> i1[0] == i2[0] ? i1[1] - i2[1] : i2[0] - i1[0]);
            count = 0;
            for (int j=0;j<temp.size();j++) {
                int[] getIndex = new int[]{temp.get(j)[0], temp.get(j)[1]};
                tempAnswer.add(getIndex[1]);
                count++;
                if (count == 2) {
                    break;
                }
            }
        }
        
        // 리턴할 answer 배열 생성
        int[] answer = new int[tempAnswer.size()];
        
        for (int i=0;i<answer.length;i++) {
            answer[i] = tempAnswer.get(i);
        }
        
        return answer;
    }
}