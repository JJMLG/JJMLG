import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        Map<String, Integer> map = new HashMap<>();
        for (String[] cloth : clothes) {
            String type = cloth[1];
            map.put(type, map.getOrDefault(type, 0) + 1);
        }

        int answer = 1;
        for (int value : map.values()) {
            //입지 않은 경우 때문에 +1
            answer *= (value + 1);
        }
        // 마지막에 모두 안입었을 경우는 안되니까 전체 수 -1
        return answer - 1;
    }
}



// import java.util.*;
// import static java.util.stream.Collectors.*;

// class Solution {
//     public int solution(String[][] clothes) {
//         return Arrays.stream(clothes)
//                 .collect(groupingBy(p -> p[1], mapping(p -> p[0], counting())))
//                 .values()
//                 .stream()
//                 .collect(reducing(1L, (x, y) -> x * (y + 1))).intValue() - 1;
//     }
// }

// import java.util.HashMap;
// import java.util.Iterator;
// class Solution {
//     public int solution(String[][] clothes) {
//         int answer = 1;
//         HashMap<String, Integer> map = new HashMap<>();
//         for(int i=0; i<clothes.length; i++){
//             String key = clothes[i][1];
//             if(!map.containsKey(key)) {
//                 map.put(key, 1);
//             } else {
//                 map.put(key, map.get(key) + 1);
//             }
//         }
//         Iterator<Integer> it = map.values().iterator();
//         while(it.hasNext()) {
//             answer *= it.next().intValue()+1;
//         }
//         return answer-1;
//     }
// }
