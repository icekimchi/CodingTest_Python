class Solution {
    
    public void getArray(int[][] an, int n){
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++)
                System.out.print(an[i][j]);
            System.out.println();
        }
    }
    
    public int[][] solution(int n) {
        int[][] answer = new int[n][n];
        int a = 1;
        
        for(int k=0; k<n/2; k++){
            for(int x=k; x<n-k; x++){
                answer[k][x] = a;
                a++;
            }
            for(int x=k+1; x<n-k; x++){
                answer[x][n-k-1] = a;
                a++;
            }
            for(int x=n-k-2; x>=k; x--){
                answer[n-k-1][x] = a;
                a++;
            }
            for(int x=n-k-2; x>=k+1; x--){
                answer[x][k] = a;
                a++;
            }
        }
        
        if(n%2!=0)
            answer[n/2][n/2] = a;
        
        getArray(answer, n);
        
        return answer;
    }
}