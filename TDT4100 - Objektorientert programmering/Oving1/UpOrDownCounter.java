package stateandbehavior;

public class UpOrDownCounter {
    int counter;
    int end;
    
    public UpOrDownCounter(int start, int end) {
	if (start == end) {
	    throw new IllegalArgumentException("De to tallene kan ikke være like!");
	}
	this.counter = start;
	this.end = end;
    }
    
    int getCounter() {
	return this.counter;
    }
    
    boolean count() {
	if (this.counter < this.end) {
	    this.counter += 1;
	    return !(this.counter==this.end);
	}
	else if (this.counter > this.end) {
	    this.counter += -1;
	    return !(this.counter==this.end);
	}
	return false;
    }
    
    
    public static void main(String[] args) {
	UpOrDownCounter c1 = new UpOrDownCounter(0, 4);
	System.out.println(c1.getCounter());
	System.out.println(c1.count());
	System.out.println(c1.getCounter());
	System.out.println(c1.count());
	System.out.println(c1.getCounter());
	System.out.println(c1.count());
	System.out.println(c1.getCounter());
	System.out.println(c1.count());
	System.out.println(c1.getCounter());
	
    }
}
