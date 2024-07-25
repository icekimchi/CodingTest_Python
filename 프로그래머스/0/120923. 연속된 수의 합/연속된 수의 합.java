class Solution {
    public int[] solution(int num, int total) {
        int[] answer = new int[num];
        int middle = 0;
        
        
        if (num%2!=0) middle = total/num; 
        else middle = (total+num/2)/num;

        for(int i=0; i<num; i++){
            answer[i] = middle-(int)num/2+i;
        }
        
    
        return answer;
    }
}