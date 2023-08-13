import java.util.*;

public class Main {

    static int total;
    static HashMap<String, Integer> map = new HashMap<String, Integer>();

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        while (scanner.hasNext()) {
            String word = scanner.nextLine();

            if (!map.containsKey(word)) {
                map.put(word, Integer.valueOf(0));
            }
            map.put(word, map.get(word) + 1);
            total++;
        }
        scanner.close();

        List<String> list = new ArrayList<String>();
        for (String s : map.keySet()) {
            list.add(s);
        }

        Collections.sort(list);

        for (int i = 0; i < list.size(); i++) {
            String name = list.get(i);
            int cnt = map.get(name);
            System.out.println(name + " " + String.format("%.4f", ((double) cnt * 100) / (double) total));
        }
    }
}
