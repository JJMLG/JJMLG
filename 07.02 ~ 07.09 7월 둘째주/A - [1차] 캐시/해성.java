import java.util.*;
class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        if(cacheSize==0) return cities.length*5;
        LinkedList<String> caches = new LinkedList<>();
        for(int i=0; i< cities.length; i++){
            String findCities = cities[i].toUpperCase();
            if(caches.contains(findCities)){
                caches.remove(caches.indexOf(findCities));
                caches.add(findCities);
                answer++;
            }else{
                if(caches.size()>=cacheSize){
                    caches.remove();
                    caches.add(findCities);
                    answer+=5;
                }else{
                    caches.add(findCities);
                    answer+=5;
                }
            }
        }
        return answer;
    }
}