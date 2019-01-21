package encapsulation;

public class Account {
    private double balance;
    private double interestRate;
    
    public Account(double balance, double interestRate) {
	this.deposit(balance);
	this.setInterestRate(interestRate);
    }
    
    public void deposit(double amount) {
	if (amount < 0) {
	    throw new IllegalArgumentException("Beløpet må være positivt");
	}
	this.balance = balance + amount;
    }
    
    public double getBalance() {
	return balance;
    }
    
    public void setInterestRate(double interestRate) {
	if (interestRate < 0) {
	    throw new IllegalArgumentException("Rentefoten må være positiv!");
	}
	this.interestRate = interestRate;
    }
    
    public double getInterestRate() {
	return interestRate;
    }
    
    public void withdraw(double amount) {
	if (amount < 0) {
	    throw new IllegalArgumentException("Beløpet må være positivt!");
	}
	if (amount > balance) {
	    throw new IllegalArgumentException("Saldoen er for lav for å ta ut dette beløpet!");
	}
	balance = balance - amount;
    }
    
    public void addInterest() {
	this.deposit(balance*interestRate*0.01);
    }
}
