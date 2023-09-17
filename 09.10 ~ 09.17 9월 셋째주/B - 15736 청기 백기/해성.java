import java.io.InputStreamReader;
import java.io.BufferedReader;
public class Main {
    public static void main(String[] args) throws Exception{
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int count =1;
        for(int i=2; i<= N; i++){
            if(i*i>N){
                break;
            }
            count++;
        }
        System.out.println(count);
    }
}
