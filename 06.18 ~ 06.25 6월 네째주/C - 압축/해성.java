import java.util.*;

class Solution {
    public int[] solution(String msg) {
        HashMap<String, Integer> map = new HashMap<>();
        ArrayList<Integer> answer = new ArrayList<>();
        for(char i = 'A'; i <= 'Z'; i++) {
            map.put(Character.toString(i), i - 'A' + 1);
        }
        int idx = 27;
        int i = 0;
        while(i < msg.length()) {
            String word = Character.toString(msg.charAt(i));
            while(map.containsKey(word)) {
                i++;
                if(i == msg.length()) {
                    break;
                }
                word += msg.charAt(i);
            }
            if(i == msg.length()) {
                answer.add(map.get(word));
                break;
            } else {
                answer.add(map.get(word.substring(0, word.length() - 1)));
                map.put(word, idx++);
            }
        }
        int[] result = new int[answer.size()];
        for(int j = 0; j < answer.size(); j++) {
            result[j] = answer.get(j);
        }
        return result;
    }
}
