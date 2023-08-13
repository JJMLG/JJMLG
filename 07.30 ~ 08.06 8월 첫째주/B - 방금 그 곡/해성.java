class Solution {
    public String solution(String m, String[] musicinfos) {
        String answer = "(None)";
        int time = 0;

        m = edit(m);

        for (int i = 0; i < musicinfos.length; i++) {

            String[] info = musicinfos[i].split(",");

            int start = (60 * Integer.parseInt(info[0].substring(0, 2)) + Integer.parseInt(info[0].substring(3)));
            int end = (60 * Integer.parseInt(info[1].substring(0, 2)) + Integer.parseInt(info[1].substring(3)));
            int t = end - start;

            if (t > time) {
                info[3] = edit(info[3]);
                StringBuffer sb = new StringBuffer();
                for (int j = 0; j < t; j++) {
                    sb.append(info[3].charAt(j % (info[3].length())));
                }
                if (sb.toString().indexOf(m) >= 0) {
                    answer = info[2];
                    time = t;
                }
            }
        }

        return answer;
    }

    public String edit(String m) {
        System.out.println("시작");
        m = m.replaceAll("C#", "H");
        System.out.println(m);
        m = m.replaceAll("D#", "I");
        System.out.println(m);
        m = m.replaceAll("F#", "J");
        System.out.println(m);
        m = m.replaceAll("G#", "K");
        System.out.println(m);
        m = m.replaceAll("A#", "L");
        System.out.println(m);
        
        return m;
    }
}