class Solution {
    public int[] solution(int[] sequence, int k) {
        int[] answer = {};
        int start=0;
        int end=0;
        int sums = sequence[start];
        int maxx = sequence.length+1;
        while(start< sequence.length && end <sequence.length){
            if(sums<k){
                end++;
                if(end==sequence.length) break;
                sums += sequence[end];
            }
            else if (sums==k){
                if(end-start+1 < maxx){
                    answer = new int[]{start, end};
                    maxx = end-start+1;
                }
                sums-=sequence[start];
                start++;
            }else{
                sums-=sequence[start];
                start++;
            }
        }
        return answer;
    }
}