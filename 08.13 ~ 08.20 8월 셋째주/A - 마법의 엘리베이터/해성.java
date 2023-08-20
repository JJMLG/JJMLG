class Solution {
    public int solution(int storey) {
        int answer = 0;
        while (storey > 0) {
            int digits = Integer.toString(storey).length();
            int closestPowerOfTen = (int) Math.pow(10, digits - 1);
            System.out.println(storey - closestPowerOfTen + " " + (Math.pow(10, digits) - storey));

            if (storey - closestPowerOfTen <= Math.pow(10, digits) - storey) {
                storey -= closestPowerOfTen;
            } else {
                storey = (int) Math.pow(10, digits) - storey;
            }
            answer++;
            System.out.println(storey+ " " + answer);
        }
        return answer;
    }
}