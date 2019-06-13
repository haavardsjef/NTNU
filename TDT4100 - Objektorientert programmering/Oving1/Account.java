package stateandbehavior;

public class Account {
    double balance;
    double interestRate;
        
    public Account() {
	
    }
    
    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }

    public double getInterestRate() {
        return interestRate;
    }

    public void setInterestRate(double interestRate) {
        this.interestRate = interestRate;
    }
    
    public void deposit(double amount) {
	if (amount>0) {
	    setBalance(this.balance + amount);
	}
	
    }
    
    public void addInterest() {
    	deposit(this.balance * this.interestRate*0.01);
    }
    
    public String toString() {
	return "Kontobalanse: " + this.getBalance() + "\n" + "Rentefot: " + this.getInterestRate();
    }

    public static void main(String[] args) {
	Account ac1 = new Account();
	System.out.println(ac1.toString());
	ac1.deposit(1000);
	System.out.println(ac1.toString());
	ac1.setInterestRate(10);
	System.out.println(ac1.toString());
	ac1.addInterest();
	System.out.println(ac1.toString());
	
	
    }
}
