package backjoon.bj20231201;

import java.io.*;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class bj2346 {
//    public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        LinkedList<int[]> list = new LinkedList<>();
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            list.add(new int[]{i + 1, Integer.parseInt(st.nextToken())});
        }

        int currentIndex = 0;
        while (!list.isEmpty()) {
            int[] current = list.remove(currentIndex);
            sb.append(current[0]).append(" ");

            if (list.isEmpty()) break;

            int move = current[1];
            if (move > 0) {
                currentIndex = (currentIndex + move - 1) % list.size();
            } else {
                currentIndex = (currentIndex + move) % list.size();
                if (currentIndex < 0) {
                    currentIndex += list.size();
                }
            }
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}
