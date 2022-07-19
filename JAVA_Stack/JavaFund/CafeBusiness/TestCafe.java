import java.util.ArrayList;
import java.util.Arrays;

public class TestCafe {
    public static void main(String[] args){
        CafeUtil appTest = new CafeUtil();
        int reward = appTest.getStreakGoal();
        // System.out.println(reward);
        System.out.println("\n----- Streak Goal Test -----");
        System.out.printf("Purchases needed by week 10: %s \n\n", appTest.getStreakGoal());
        System.out.println("----- Order Total Test-----");
        double[] lineItems = {3.5, 1.5, 4.0, 4.5};
        System.out.printf("Order total: %s \n\n",appTest.getOrderTotal(lineItems));
        
        double total = appTest.getOrderTotal(lineItems);
        System.out.println(total);

        System.out.println("----- Display Menu Test-----");

        ArrayList<String> menu = new ArrayList<String>();
        menu.add("Latte");
        menu.add("Cap");
        menu.add("Drip");
        appTest.displayMenu(menu);

        System.out.println("\n----- Add Customer Test-----");

        ArrayList<String> customers = new ArrayList<String>();
          // --- Test 4 times ---
        customers.add("Aziza");
        customers.add("Awatif");
        customers.add("Zainb");
        for (int i = 0; i < 4; i++) {
            // appTest.addCustomer(customers);
            System.out.println("\n");
        appTest.addCustomer(customers);
        }
    }
}