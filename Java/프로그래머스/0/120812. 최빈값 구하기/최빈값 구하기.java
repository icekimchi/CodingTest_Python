import java.util.*;

class Solution {
    public int solution(int[] array) {
        
        Map<Integer, Integer> countHash = new HashMap<>();
        int answer = 0;
        
        // 각 원소의 개수를 세는 부분
        for(int key: array){
            if (countHash.containsKey(key))
                countHash.replace(key, countHash.get(key)+1);
            else
                countHash.put(key, 1);
        }
        
        System.out.println(countHash);
        
        // 최빈값을 구하는 코드
        int max = Collections.max(countHash.values());
        int cnt = 0;
        for (int key: countHash.keySet()) {
			if (countHash.get(key)==max){
                cnt += 1;
                answer = key;
            }
		}
        
        return cnt==1 ? answer:-1;
    }
}