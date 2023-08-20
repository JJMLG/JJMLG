import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());

        int[] trees = new int[n];
        for (int i = 0; i < n; i++) {
            trees[i] = Integer.parseInt(br.readLine());
        }

        long maxProfit = Long.MIN_VALUE;

        for (int L = 1; L <= getMax(trees); L++) {
            long currentProfit = 0;
            for (int tree : trees) {
                int pieces = tree / L;
                long profitFromSelling = (long) pieces * L * w;
                long cost = (long) (pieces - (tree % L == 0 ? 1 : 0)) * c;
                if(profitFromSelling - cost > 0) {
                    currentProfit += profitFromSelling - cost;
                }
            }
            maxProfit = Math.max(maxProfit, currentProfit);
        }

        System.out.println(maxProfit);
    }

    private static int getMax(int[] array) {
        int max = Integer.MIN_VALUE;
        for (int num : array) {
            if (num > max) {
                max = num;
            }
        }
        return max;
    }
}
