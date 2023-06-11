import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        int left = 0;
        int right = 9;
        Map<String, Integer> map = new HashMap<>();
        //discount 개수
        for(int i =0;i<10;i++) {
            map.put(discount[i], map.getOrDefault(discount[i],0)+1);
        }
        while(right < discount.length){
            if(check(map,want,number)) {
                answer++;
            }
            right++;
            if(right < discount.length) {
                map.put(discount[right], map.getOrDefault(discount[right],0)+1);
            }
            map.put(discount[left], map.get(discount[left])-1);
            if(map.get(discount[left]) == 0) {
                map.remove(discount[left]);
            }
            left++;
        }

        return answer;
    }
    private boolean check(Map<String,Integer> map,String[] want,int[] number){
        for(int i =0;i<want.length;i++){
            if(map.getOrDefault(want[i],0) < number[i]) return false;
        }
        return true;
    }
}