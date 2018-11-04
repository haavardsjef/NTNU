class Account{

    static double balance;
    static float interestRate;
    public static void deposit(double ammount){
        if (ammount > 0){
            balance = balance + ammount;
        }
    }

    public static void addInterest(){
        deposit(balance * interestRate);
    }

    public static double getBalance(){
        return balance;
    }
    public static float getInterestRate(){
        return interestRate;
    }
    public static void setInterestRate(float newRate){
        interestRate = newRate;
    }







    public static void main(String[] args) {
        deposit(15);
        deposit(-3);
        interestRate = 0.04f;
        System.out.println(getBalance());
        addInterest();
        System.out.println(getBalance());
    }
}
