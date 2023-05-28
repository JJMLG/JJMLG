import java.util.*;

class Solution {
    public int check(Deque<Character> deq){
        Deque<Character> copydeq = new LinkedList<>();
        copydeq.addAll(deq);
        Stack<Character> stk = new Stack<>();
        int SIZE_DQ = deq.size();
        for(int i = 0; i < SIZE_DQ; i++){
            char front = copydeq.removeFirst();
            if(front == '[' || front == '(' || front == '{'){
                stk.add(front);
            } else {
                if(stk.isEmpty()){
                    return 0;
                }
                if(front == '}'){
                    if(stk.peek() == '{'){
                        stk.pop();
                    } else {
                        return 0;
                    }
                } else if(front == ']'){
                    if(stk.peek() == '['){
                        stk.pop();
                    } else {
                        return 0;
                    }
                } else if(front == ')'){
                    if(stk.peek() == '('){
                        stk.pop();
                    } else {
                        return 0;
                    }
                }
            }
        }
        return stk.isEmpty() ? 1 : 0;
    }

    public int solution(String s) {
        int answer = 0;
        Deque<Character> dq = new LinkedList<>();
        for(int i = 0; i < s.length(); i++){
            dq.addLast(s.charAt(i));
        }
        answer += check(dq);
        for(int i = 1; i < s.length(); i++){
            dq.addFirst(dq.removeLast());
            answer += check(dq);
        }
        return answer;
    }
}
