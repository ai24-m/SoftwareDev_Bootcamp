public class BankAccountTest {
    public static void main(String[] args) {
        BankAccount account1 = new BankAccount();
        BankAccount account2 = new BankAccount();
        BankAccount account3 = new BankAccount();
        BankAccount account4 = new BankAccount();

        System.out.println("\n________________________________________________\n");
        System.out.println("\nBank Total Amount :"+BankAccount.getAmountOfMoney());
        System.out.println("The Accounts Number:  "+BankAccount.accountCount());
        System.out.println("\n________________________________________________\n");

        System.out.println("\nThe Total Amount Befor Deposit Of Account1 :  "+ account1.getAmountTotal());
        System.out.println("\n________________________________________________\n");

        System.out.println("\nDeposit 20 to Checking Balance and 30 to Savings Balance for the Account 1 : ");
        account1.deposit("checkingBalanc",20);
        account1.deposit("savingsBalance",30);
        System.out.println("\n________________________________________________\n");
        System.out.println("\nThe Total Amount of Account1 After Deposit :  "+ account1.getAmountTotal());
        System.out.println("\n________________________________________________\n");


        System.out.println("\nDeposit 0 to Checking Balance and 70 to Savings Balance for the Account 2 : ");
        account2.deposit("checkingBalanc",0);
        account2.deposit("savingsBalance",70);
        System.out.println("\n________________________________________________\n");
        System.out.println("\nThe Total Amount of Account2 after Deposit :  "+ account2.getAmountTotal());

        System.out.println("\n________________________________________________\n");
        System.out.println("\n****** Withdraw 5 ****** \n"); 
        account1.withdraw("checkingBalanc",5);
        System.out.println("The Total Amount of Account1 After Withdraw :  "+ account1.getAmountTotal());

        System.out.println("\n________________________________________________\n");
        System.out.println("\n******  Withdraw 50 ******\n"); 
        account1.withdraw("checkingBalanc",50);
        System.out.println("");

        System.out.println("\nThe Total Mount of Account1 :  "+ account1.getAmountTotal());
        System.out.println("\n________________________________________________\n");

        System.out.println("Bank Total Amount : "+BankAccount.getAmountOfMoney());
        System.out.println("");

    }

}
