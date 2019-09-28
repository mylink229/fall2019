public class DateAndTime {
    private int sec;
    private int hr;
    private int min;

    private int d;
    private int m;
    private int y;

    public DateAndTime(
        int sec,
        int min,
        int hr,
        int d,
        int m,
        int y
    ) throws OutOfBounds{
        if (
            sec > 59||
            min > 59||
            hr > 12||
            hr == 0||
            d == 0||
            m == 0||
            y == 0
        ) {
            throw new OutOfBounds("Attributes are not valid.");
        } else {
            this.sec = sec;
            this.min = min;
            this.hr = hr;

            this.d = d;
            this.m = m;
            this.y = y;
        }
    }

    public void incrementSec() {
        this.sec++;

        if (this.sec >= 60) {
            this.sec = 1;
            incrementMin();
        }
    }

    public void incrementMin() {
        this.min++;

        if (this.min >= 60) {
            this.min = 1;
            incrementHr();
        }
    }

    public void incrementHr() { 
        this.hr++;

        if (this.hr >= 12) {
            this.hr = 1;
            incrementDay();
        }
    }

    public void incrementDay() {
        this.d++;

        if (this.d > 31) {
            this.d = 1;
            incrementMonth();
        }
    }
 
    public void incrementMonth() {
        this.m++;

        if (this.m > 12) {
            this.m = 1;
            incrementYear();
        }
    }

    public void incrementYear() {
        this.y++;
    }

    public String toString() {
        String totalStr = String.format(
            "%1$d:%2$d:%3$d  %4$d/%5$d/%6$d", 
            this.sec,
            this.min,
            this.hr,

            this.d,
            this.m,
            this.y
        );
        return totalStr;
    }
}