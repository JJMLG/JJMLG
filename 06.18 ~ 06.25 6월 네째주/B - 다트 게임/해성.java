import java.util.*;

class Solution {
    public int solution(String dartResult) {
        int answer = 0;
        Stack<Integer> STK = new Stack<Integer>();
        for (int i = 0; i < dartResult.length(); i++) {
            int temp=0;
            char dart = dartResult.charAt(i);
            if(Character.isDigit(dart)) {
                temp+= (dart-'0');
                if(dart=='1'&& i< dartResult.length()-1 && dartResult.charAt(i+1)=='0'){
                    temp=10;
                    i++;
                }
                STK.push(temp);
            }
            else{
                if (dart == 'D') {
                    temp = STK.pop();
                    STK.push((int)Math.pow(temp,2));
                }
                else if (dart == 'T'){
                    temp = STK.pop();
                    temp = (int) Math.pow(temp,3);
                    STK.push(temp);
                } 
                else if (dart == '*'){
                    int prevScore = STK.pop()*2;
                    if(!STK.isEmpty()) {
                        int beforeScore = STK.pop()*2;
                        STK.push(beforeScore);
                    }
                    STK.push(prevScore);
                } 
                else if (dart == '#') {
                    temp = STK.pop();
                    STK.push(temp* (-1));
                }
            }
        }
        while(!STK.isEmpty()){
            answer+=STK.pop();
        }
        return answer;
    }
}