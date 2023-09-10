import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map.Entry;

public class bj2608 {
    static HashMap<String, Integer> map;
    static int ans1 =0;
    static String ans2 = "";
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String A[]= in.readLine().split("");
        String B[]= in.readLine().split("");
        map= new HashMap<String,Integer>();
        map.put("I", 1);
        map.put("IV", 4);
        map.put("V", 5);
        map.put("IX", 9);
        map.put("X", 10);
        map.put("XL", 40);
        map.put("L", 50);
        map.put("XC", 90);
        map.put("C", 100);
        map.put("CD", 400);
        map.put("D", 500);
        map.put("CM", 900);
        map.put("M", 1000);
        makeNum(A);
        makeNum(B);
        makeString(ans1);
        System.out.println(ans1);
        System.out.println(ans2);
    }
    private static void makeString(int num){
        List<Entry<String, Integer>> list = new ArrayList<>(map.entrySet());
        list.sort(Entry.comparingByValue(Collections.reverseOrder()));
        while(num!=0){
            int quo = 0;
            for (Entry<String, Integer> entry : list){
                quo = num/entry.getValue();
                if(quo !=0){
                    for (int i=0; i< quo; i++){
                        ans2+= entry.getKey();
                    }
                    num = num%entry.getValue();
                    break;
                }
            }
        }
    }
    private static void makeNum(String[] arr){
        for (int i=0; i< arr.length; i++){
            char c = arr[i].charAt(0);
            if ((c=='I'|| c== 'X' || c == 'C') && i<arr.length-1){
                String s = arr[i] + arr[i+1];
                if(map.containsKey(s)){
                    ans1+=map.get(s);
                    i++;
                    continue;
                }
            }
            ans1 += map.get(arr[i]);
        }
    }
}
