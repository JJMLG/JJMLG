import java.util.*;

class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        HashMap<Character, Integer> hm = new HashMap<>();
        ArrayList<Integer> answerList = new ArrayList<>();
        for(int i=0; i<keymap.length; i++) {
            int a =0;
        	for(int j=0; j<keymap[i].length(); j++) {
                Character cc = keymap[i].charAt(j);
                if(hm.get(cc)!=null && hm.get(cc) > j+1){
                   hm.put(keymap[i].charAt(j), j+1);
                }else if(hm.get(cc)==null){
                    hm.put(keymap[i].charAt(j), j+1);
                };
            }
        }
        for(int k=0; k< targets.length; k++){
            int aa=0;
            for(int c=0; c< targets[k].length(); c++){
                if(hm.get(targets[k].charAt(c))==null){
                    aa=-1;
                    break;
                }
                aa+=hm.get(targets[k].charAt(c));
            }
            answerList.add(aa);
        }
        int[] answer = answerList.stream().mapToInt(i -> i).toArray();
        return answer;
    }
}