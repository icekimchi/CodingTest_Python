import java.util.*;

class Solution {
    public String[] solution(String[] quiz) {
        String[] answer = new String[quiz.length];
        int a, b;
        
        for(int i=0; i<quiz.length; i++){
            String strings[] = quiz[i].split(" ");
            
            a = Integer.parseInt(strings[0]);
            b = Integer.parseInt(strings[2]);
            
            if (strings[1].equals("+"))
                 answer[i] = (a+b)==(Integer.parseInt(strings[4])) ? "O" : "X";
            else
                 answer[i] = (a-b)==(Integer.parseInt(strings[4])) ? "O" : "X";
        }
       
        return answer;
    }
}