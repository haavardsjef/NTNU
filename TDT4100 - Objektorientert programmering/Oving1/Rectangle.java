package stateandbehavior;


public class Rectangle {
    Integer MinX;
    Integer MaxX;
    Integer MinY;
    Integer MaxY;
    
    public Rectangle() {
    }
    
    public int getMinX() {
	if (MinX == null) {
	    return 0;
	}
        return MinX;
    }

    public int getMaxX() {
	if (MaxX == null) {
	    return 0;
	}
        return MaxX;
    }

    public int getMinY() {
	if (MinY == null) {
	    return 0;
	}
        return MinY;
    }

    public int getMaxY() {
	if (MaxY == null) {
	    return 0;
	}
        return MaxY;
    }
    
    public int getHeight() {
	if (MinY==null) {
	    return 0;
	}
	return getMaxY()-getMinY() +1;
    }
    
    public int getWidth() {
	if(MinX == null) {
	    return 0;
	}
	return getMaxX()-getMinX() +1;
    }
    
    public boolean isEmpty() {
	return (getWidth()==0 && getHeight()==0);
    }
    
   
    // Checks if the rectangle contains the point(x,y)
   public boolean contains(int x, int y) {
       if (isEmpty()) {
	   return false;
       }
       return (x >= getMinX() && x <= getMaxX() && y >= getMinY() && y <= getMaxY());
   }
   
   // Checks if the rectangle contains the rectangle "rect" within itself
   public boolean contains(Rectangle rect) {
       return (this.contains(rect.getMinX(), rect.getMinY()) && this.contains(rect.getMaxX(), rect.getMaxY()));
   }
   
   
   // Method to add a point (x,y) to the rectangle.
   public boolean add(int x, int y) {
       if (contains(x,y)) {
	   return false;
       }
       if (isEmpty()) {
	   this.MinX = x;
	   this.MaxX = x;
	   this.MinY = y;
	   this.MaxY = y;
	   return true;
       }
       if (x < getMinX()) {
	   this.MinX = x;
       }
       if (x > getMaxX()) {
	   this.MaxX = x;
       }
       if (y < getMinY()) {
	   this.MinY = y;
       }
       if (y > getMaxY()) {
	   this.MaxY = y;
       }
       return true;
       
   }
   // Adds the entire rectangle rect
   public boolean add(Rectangle rect) {
       if (this.contains(rect)) {
	   return false;
       }
       if (rect.getMinX() < this.getMinX()) {
	   this.MinX = rect.getMinX();
       }
       if (rect.getMaxX() > this.getMaxX()) {
	   this.MaxX = rect.getMaxX();
       }
       if (rect.getMinY() < this.getMinY()) {
	   this.MinY = rect.getMinY();
       }
       if (rect.getMaxY() > this.getMaxY()) {
	   this.MaxY = rect.getMaxY();
       }
       return true;
   }
   
   
   //Returnerer det minste rektanglet som også inneholder rect.
   public Rectangle union(Rectangle rect) {
       Rectangle temp = new Rectangle();
       temp.add(this);
       temp.add(rect);
       return temp;
   }
   
   
   public String getExtremes() {
       return ("Minimum X: " + MinX + "\n"
	       + "Maximum X: " + MaxX + "\n"
	       + "Minimum Y: " + MinY + "\n"
	       + "Maximum Y: " + MaxY);
   }
    
    public static void main(String[] args) {
	Rectangle rec1 = new Rectangle();
	
	// Empty rectangle
	System.out.println(rec1.getExtremes());
	System.out.println("Is empty: " + rec1.isEmpty());
	System.out.println("getMinX: " + rec1.getMinX());
	System.out.println("Width: " + rec1.getWidth());
	System.out.println("Height: " + rec1.getHeight());
	System.out.println("Contains (0,0): " + rec1.contains(0, 0));
	System.out.println("");
	
	System.out.println("--");
	System.out.println("Adding (0,0): " + rec1.add(0, 0));
	System.out.println("--");
	
	// After adding (0,0)
	System.out.println(rec1.getExtremes());
	System.out.println("Is empty: " + rec1.isEmpty());
	System.out.println("getMinX: " + rec1.getMinX());
	System.out.println("Width: " + rec1.getWidth());
	System.out.println("Height: " + rec1.getHeight());
	System.out.println("Contains (0,0): " + rec1.contains(0, 0));
	System.out.println("");
	
	System.out.println("--");
	System.out.println("Adding (3,5): " + rec1.add(3, 5));
	System.out.println("--");
	
	// After adding (3,5)
	System.out.println(rec1.getExtremes());
	System.out.println("Width: " + rec1.getWidth());
	System.out.println("Height: " + rec1.getHeight());
	System.out.println("");
	
	System.out.println("--");
	System.out.println("Adding (2,2): " + rec1.add(2, 2));
	System.out.println("--");
	
	// After "adding" (2,2)
	System.out.println(rec1.getExtremes());
	System.out.println("");
	
	
	
	// Making two new rectangles
	System.out.println("Creating rec2 and rec 3");
	Rectangle rec2 = new Rectangle();
	rec2.add(0, 2);
	rec2.add(8,4);
	
	Rectangle rec3 = new Rectangle();
	rec3.add(2, 0);
	rec3.add(4,8);
	
	System.out.println("\n");
	System.out.println("rec2:");
	System.out.println(rec2.getExtremes());
	System.out.println("Contains rec1: " + rec2.contains(rec1));
	System.out.println("Contains rec2: " + rec2.contains(rec2));
	System.out.println("Add rec2: " + rec2.add(rec2));
	
	System.out.println("\n");
	System.out.println("rec3:");
	System.out.println(rec3.getExtremes());
	System.out.println("Add rec2: " + rec3.add(rec2));
	System.out.println(rec3.getExtremes());
    }
    
}
