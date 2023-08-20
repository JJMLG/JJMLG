import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder("");

    static int N, K, A, B, ans = 1;
    static int[] pots;

    static void input() throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        A = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());
        pots = new int[N];
        Arrays.fill(pots, K);
    }

    // 연속된 A개의 화분 중에서 수분의 합이 가장 적은 구간의 시작 인덱스를 반환
    static int findMinSegment() {
        int startIdx = 0;
        int currentSum = 0;
        for (int i = 0; i < A; i++) {
            currentSum += pots[i];
        }

        int minSum = currentSum;

        for (int i = A; i < N; i++) {
            currentSum = currentSum - pots[i - A] + pots[i];
            if (currentSum < minSum) {
                minSum = currentSum;
                startIdx = i - A + 1;
            }
        }
        return startIdx;
    }

    static void process(){
        while(true){
            int index = findMinSegment();
            for(int i=index; i<index+A; i++) pots[i%N] += B;
            for(int i=0; i<N; i++){
                if(--pots[i] == 0){
                    System.out.println(ans);
                    return;
                }
            }
            ans += 1;
        }
    }

    public static void main(String[] args) throws IOException{
        input();
        process();
    }
}
