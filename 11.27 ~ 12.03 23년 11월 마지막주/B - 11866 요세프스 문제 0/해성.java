package backjoon.bj20231201;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class bj11866 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stk =new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(stk.nextToken());
        int K = Integer.parseInt(stk.nextToken());
        ArrayList<Integer> list = new ArrayList<>(N);
        StringBuilder sb = new StringBuilder();
        sb.append("<");
        int cnt = 1, idx = 0;
        for(int i=1; i<=N; i++){
            list.add(i);
        }
        while(list.size() !=0){
            if(idx>=list.size()){
                idx=0;
            }
            if(cnt==K){
                sb.append(list.remove(idx));
                cnt=1;
                if(list.size()==0){
                    sb.append(">");
                }else{
                 sb.append(", ");
                }
            }else{
                idx++;
                cnt++;
            }
        }
        System.out.println(sb);
    }
}
