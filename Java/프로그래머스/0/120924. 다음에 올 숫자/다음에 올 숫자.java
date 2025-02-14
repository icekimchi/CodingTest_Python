class Solution {
    public int solution(int[] common) {
        //등차수열인지 확인
        if(common[0]-common[1] == common[1]-common[2]){
            return common[common.length-1] + (common[2]-common[1]);
        }else{
            return common[common.length-1] * (common[2]/common[1]);
        }
    }
}