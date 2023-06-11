class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int[] students = new int[n];
        
        // 모든 학생은 체육복 1벌을 가지고 시작함
        for (int i = 0; i < n; i++) {
            students[i] = 1;
        }
        
        // 체육복을 잃어버린 학생은 -1
        for (int i = 0; i < lost.length; i++) {
            students[lost[i] - 1]--;
        }
        
        // 체육복을 여분으로 가진 학생은 +1
        for (int i = 0; i < reserve.length; i++) {
            students[reserve[i] - 1]++;
        }
        
        // 체육복을 빌려줄 수 있는 경우를 처리
        for (int i = 0; i < n; i++) {
            if (students[i] == 0) {
                if (i > 0 && students[i - 1] == 2) {
                    students[i]++;
                    students[i - 1]--;
                } else if (i < n - 1 && students[i + 1] == 2) {
                    students[i]++;
                    students[i + 1]--;
                }
            }
        }
        
        // 체육복을 입을 수 있는 학생 수 계산
        int answer = 0;
        for (int i = 0; i < n; i++) {
            if (students[i] > 0) {
                answer++;
            }
        }
        
        return answer;
    }
}
