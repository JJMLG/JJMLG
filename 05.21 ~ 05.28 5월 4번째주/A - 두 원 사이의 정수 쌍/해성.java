class Solution {
    public long solution(int r1, int r2) {
        long answer = 0;

        for (int i = 1; i <= r2; i++) {
            int start = (int) Math.ceil(Math.sqrt((long) r1 * r1 - (long) i * i));
            int end = (int) Math.floor(Math.sqrt((long) r2 * r2 - (long) i * i));

            answer += end - start + 1;
        }

        return answer * 4;
    }
}
