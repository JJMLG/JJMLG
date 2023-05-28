class Solution {
    public int solution(int number, int limit, int power) {
        int answer = 0;
        int numbers[]= new int[number+1];
        for(int i=1; i<= number;i++){
            for(int j =1; j*i<= number;j++){
                if(numbers[i*j]<=limit) {
                    numbers[i*j]++;
                }
            }
        }    
        for(int i=0; i< numbers.length;i++){
            if(numbers[i]>limit){
                answer+=power;
            }else answer+= numbers[i];
        }
        return answer;
    }
}