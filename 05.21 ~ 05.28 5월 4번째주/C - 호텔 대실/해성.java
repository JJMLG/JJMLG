import java.util.*;

class Solution {
    class Book {
        private int startTime;
        private int endTime;

        public Book(int startTime, int endTime) {
            this.startTime = startTime;
            this.endTime = endTime;
        }

        public int getStartTime() {
            return startTime;
        }

        public int getEndTime() {
            return endTime;
        }
    }

    List<Book> bookList = new ArrayList<>();

    int convertToMinute(String time) {
        String[] tokens = time.split(":");
        int hour = Integer.parseInt(tokens[0]);
        int minute = Integer.parseInt(tokens[1]);
        return hour * 60 + minute;
    }

    public int solution(String[][] bookTimes) {
        for (String[] bookTime : bookTimes) {
            int startTime = convertToMinute(bookTime[0]);
            int endTime = convertToMinute(bookTime[1]);

            bookList.add(new Book(startTime, endTime));
        }

        Collections.sort(bookList, (book1, book2) -> {
            if (book1.getStartTime() == book2.getStartTime()) {
                return book1.getEndTime() - book2.getEndTime();
            } else {
                return book1.getStartTime() - book2.getStartTime();
            }
        });

        List<Integer> roomEndTimes = new ArrayList<>();

        for (Book book : bookList) {
            boolean isOk = false;
            for (int i = 0; i < roomEndTimes.size(); i++) {
                int endTime = roomEndTimes.get(i) + 10;
                if (book.getStartTime() >= endTime) {
                    roomEndTimes.set(i, book.getEndTime());
                    isOk = true;
                    break;
                }
            }
            if (!isOk) {
                roomEndTimes.add(book.getEndTime());
            }
        }

        return roomEndTimes.size();
    }
}
