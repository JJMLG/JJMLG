import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[] sour;
    static int[] bitter;
    static int res = Integer.MAX_VALUE;
    static int n;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stk;
        n = Integer.parseInt(br.readLine());
        sour = new int[n];
        bitter = new int[n];
        for(int i=0; i<n; i++){
            stk = new StringTokenizer(br.readLine());
            sour[i] = Integer.parseInt(stk.nextToken());
            bitter[i]= Integer.parseInt(stk.nextToken());
        }
        checkTaste(0, 0,1,0);
        System.out.println(res);
    }
    public static void checkTaste(int cnt, int checkCnt, int sour_sum, int bitter_sum){
        if(cnt==n){
            if(checkCnt!=0){
                res = Math.min(res, Math.abs(sour_sum - bitter_sum));
            }
            return;
        }
        checkTaste(cnt+1, checkCnt, sour_sum, bitter_sum);
        checkTaste(cnt+1, checkCnt+1, sour_sum*sour[cnt], bitter_sum+bitter[cnt]);
    }
}