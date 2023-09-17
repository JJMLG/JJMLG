import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for (int k = 0; k < t; k++) {
            int n = scanner.nextInt();
            int[] dots = new int[n];
            for (int i = 0; i < n; i++) {
                dots[i] = scanner.nextInt();
            }
            Arrays.sort(dots);
            int count = 0;
            for (int i = 0; i < dots.length; i++) {
                for (int j = i + 2; j < dots.length; j++) {
                    if ((dots[i] + dots[j]) % 2 == 0) {
                        int dot = (dots[i] + dots[j]) / 2;
                        count += checkDot(dots, dot);
                    }
                }
            }
            System.out.println(count);
        }
    }

    public static int checkDot(int[] dots, int dot) {
        int rightIndex = Arrays.binarySearch(dots, dot);
        if (rightIndex < 0) {
            return 0;
        }
        return 1;
    }
}