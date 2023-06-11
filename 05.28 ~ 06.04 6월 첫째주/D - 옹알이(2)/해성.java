class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        for(int i=0; i<babbling.length;i++){
            if(babbling[i].contains("ayaaya")) continue;
            if(babbling[i].contains("yeye")) continue;
            if(babbling[i].contains("woowoo")) continue;
            if(babbling[i].contains("mama")) continue;

            babbling[i] = babbling[i].replace("aya", " ");
            babbling[i] = babbling[i].replace("ye", " ");
            babbling[i] = babbling[i].replace("woo", " ");
            babbling[i] = babbling[i].replace("ma", " ");
            babbling[i] = babbling[i].replace(" ", "");

            if(babbling[i].length()  == 0) answer++;
        }
        
        return answer;
    }
}