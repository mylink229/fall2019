
public class Transaction {
	private int accountNumber;
	private double amount;
	
	public int getAccountNumber() {
		return accountNumber;
	}

	public void setAccountNumber(int accountNumber) {
		this.accountNumber = accountNumber;
	}

	public double getAmount() {
		return amount;
	}

	public void setAmount(double amount) {
		this.amount = amount;
	}
	
	public Transaction(int accountNumber, double amount) {
		this.accountNumber = accountNumber;
		this.amount = amount;
	}

}
