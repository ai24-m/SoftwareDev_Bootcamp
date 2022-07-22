public class BankAccount {

    private double  checkingBalance;
    private double savingsBalance;
    private static int accountCount = 0 ;

// Create a class member (static) that tracks the total amount of money stored in every account created.

    private static double amountOfMoney ;

    public BankAccount() {
        accountCount++;
    }
    public static int accountCount() {
        return accountCount;
    }
    public static double getAmountOfMoney() {
        return amountOfMoney;
    }
    public double getAmountTotal(){
        double amountTotal = savingsBalance + checkingBalance ;
        return amountTotal;
        }
    
// Create a getter method for the user's checking account balance.

    public double getCheckingBalance() {
        return checkingBalance;
    }

// Create a getter method for the user's saving account balance.
    public double getSavingsBalance() {
        return savingsBalance;
    }

// Create a method that will allow a user to deposit money into either the checking or saving, be sure to add to total amount stored.
    public void deposit(String account , double amount){
            if (amount<=0) {
                        System.out.println("\n---- Amount to be deposited should be More than 0!!! ---- ");
                    } else {
                        if(account.equals("checkingBalanc")){
                            // setCheckingBalance(amount);
                            checkingBalance = amount;
                            amountOfMoney+=checkingBalance;
                        }
                        else if(account.equals("savingsBalance")){
                            savingsBalance = amount;
                            amountOfMoney+=savingsBalance;
                        }
                    }
        }

// Create a method to withdraw money from one balance. Do not allow them to withdraw money if there are insufficient funds.
    public void withdraw(String account , double amount){
        if(account.equals("checkingBalanc")){
            if(amount<= checkingBalance){
                checkingBalance -= amount;
                amountOfMoney -= amount;
            }else{
                System.out.println("\n--- Insufficient balance !! ---");
            }
        }
        else if(account.equals("savingsBalance")){
            if(amount<= savingsBalance){
                savingsBalance -= amount;
                amountOfMoney -= amount;
            }else{
                System.out.println("\n--- Insufficient balance !! ---");
            }
        }
        
    }

}




