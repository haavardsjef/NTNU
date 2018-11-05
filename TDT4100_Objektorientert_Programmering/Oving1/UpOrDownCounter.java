class UpOrDownCounter {

    int start;
    int end;
    int counter;

    //Constructor
    public UpOrDownCounter(int start, int end){
        this.start = start;
        this.end = end;
        this.counter = start;
    }

    public int getCounter(){
        return counter;
    }

    public boolean count(){
        if (start < end && counter != end) {
            counter++;
        }
        if (start > end && counter != end) {
            counter--;
        }

        if (counter == end) {
            return false;
        }
        else{
            return true;
        }
    }
    public static void main(String[] args) {
        UpOrDownCounter counter1 = new UpOrDownCounter(0,2);
        System.out.println(counter1.count());
        System.out.println(counter1.getCounter());
        System.out.println(counter1.count());
        System.out.println(counter1.getCounter());
        System.out.println(counter1.count());
        System.out.println(counter1.getCounter());
        System.out.println(counter1.count());
        System.out.println(counter1.getCounter());

    }
}
