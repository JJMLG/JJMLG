import java.util.*;
class Solution {
    public int[] solution(String s) {
        Set<String> set = new HashSet<>();
        String[] arr = s.replaceAll("[{]", " ").replaceAll("[}]", " ").trim().split(" , ");
        Arrays.sort(arr, (a, b)->{return a.length() - b.length();});
        int[] answer = new int[arr.length];
        int idx = 0;
        for(String s1 : arr) {
            for(String s2 : s1.split(",")) {
                if(set.add(s2)) answer[idx++] = Integer.parseInt(s2);
            }
        }
        return answer;
    }
}

// import java.util.*;

// class Solution {
//     public int[] solution(String s) {
//         HashMap<Integer, Integer> map = new HashMap<>();
//         // Remove brackets and split by comma
//         // String[] numbers = s.replaceAll("[{}]", "").split(",");
//         String[] numbers = s.replace("{", "").replace("}", "").split(",");

//         // for(int i=0; i< numbers.length;i++){
//         //     System.out.println(numbers[i]);
//         // }
//         // Count the frequency of each number
//         for (String number : numbers) {
//             int num = Integer.parseInt(number);
//             map.put(num, map.getOrDefault(num, 0) + 1);
//         }
        
//         // Sort the keys by frequency in descending order
//         List<Integer> keys = new ArrayList<>(map.keySet());
//         keys.sort((num1, num2) -> map.get(num2) - map.get(num1));
        
//         // Convert the list to an array
//         int[] answer = new int[keys.size()];
//         for (int i = 0; i < keys.size(); i++) {
//             answer[i] = keys.get(i);
//         }
        
//         return answer;
//     }
// }