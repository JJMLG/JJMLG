import java.util.*;
class Solution {
    public int solution(int[] order) {
        int cnt = 0;

        Stack<Integer> supp = new Stack<>();
        Queue<Integer> origin = new LinkedList<>();

            for(int i=0; i<order.length; i++){
                supp.add(i+1);

                while(!supp.isEmpty()){
                    if(supp.peek() == order[cnt]){
                        origin.offer(supp.pop());
                        cnt++;
                    }else break;
                }
            }
        return origin.size();
    }
}