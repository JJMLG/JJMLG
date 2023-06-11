class Solution {
    int maxx=0;
    public int solution(int k, int[][] dungeons) {
        int[] visited = new int[dungeons.length];
        dfs(dungeons, visited, 0, k);
        return maxx;
    }
    public void dfs(int[][] dungeons, int[] visited, int count, int rem){
        for(int i=0; i<dungeons.length;i++){
            if(visited[i]!=0 || rem < dungeons[i][0]) continue;
                visited[i]=1;
                dfs(dungeons, visited, count+1, rem-dungeons[i][1]);
                visited[i]=0;    
        }
        if(maxx<count) maxx=count;
    }
}