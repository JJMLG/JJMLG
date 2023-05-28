import java.util.*;
class Solution {
    public int[] solution(int k, int[] score) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int answer[]= new int[score.length];
        for(int j =0; j< score.length;j++){
            pq.add(score[j]);
            if(pq.size()>k){
                pq.poll();
            }
            answer[j] = pq.peek();
        }
        return answer;
    }
}