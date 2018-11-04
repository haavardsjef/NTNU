class Location{
    static int x;
    static int y;

    public static void up(){
        y--;
    }
    public static void down(){
        y++;
    }
    public static void right(){
        x++;
    }
    public static void left(){
        y = y - 1;
    }
    public static int getX(){
        return x;
    }
    public static int getY(){
        return y;
    }

    public static void main(String[] args) {
        up();
        System.out.println(y);
    }
}
