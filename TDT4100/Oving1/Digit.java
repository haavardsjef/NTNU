class Digit{

    int power;
    int digit;

    // Constructor
    public Digit(int power){
        this.power = power;
        digit = 0;
    }

    public int getValue(){
        return digit;
    }

    public boolean increment(){
        digit++;
        if (digit == power){
            digit = 0;
            return true;
        }
        else{
            return false;
        }
    }

    public int getBase(){
        return power;
    }


    public static void main(String[] args) {
        Digit dig1 = new Digit(2);
        dig1.increment();
        dig1.increment();
        System.out.println(dig1.getValue());
    }
}
