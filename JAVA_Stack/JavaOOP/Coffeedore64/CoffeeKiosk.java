import java.util.ArrayList;


public class CoffeeKiosk {
    // Member variables:
public ArrayList<Item> menu;
public ArrayList<Order> orders;

// Constructor - no params, initializes items and orders to empty arrays.
    public CoffeeKiosk() {
        menu = new ArrayList<Item>();
        orders = new ArrayList<Order>() ;

    }

    // The addMenuItem method should create a new item object with the given name and price.
    public void addMenuItem(String name, double price){
        Item item = new Item();
        item.setName(name);
        item.setPrice(price);
        // Add the new Item object to the menu items array
        menu.add(item);
    }

    // The displayMenu method should display all of the items from the menu array
    public void displayMenu(){
        // for loop to accept all new items in the menu array
        for(int index=0; index<menu.size(); index++){
            System.out.println(index+" "+menu.get(index).getName()+"-- $"+menu.get(index).getPrice());
        }

    }

    public void newOrder() {
        
    	// Shows the user a message prompt and then sets their input to a variable, name
        System.out.println("Please enter customer name for new order:");
        String name = System.console().readLine();
    
    	// Your code:
        // Create a new order with the given input string
        Order order = new Order();
        order.setName(name);
        
        // Show the user the menu, so they can choose items to add.
        displayMenu();
        
    	// Prompts the user to enter an item number
        System.out.println("Please enter a menu item index or q to quit:");
        String itemNumber = System.console().readLine();
        int i = Integer.parseInt(itemNumber);
        
        // Write a while loop to collect all user's order items
        while(!itemNumber.equals("q")) {
            
            // Get the item object from the menu, and add the item to the order
            i = Integer.parseInt(itemNumber);
            Item item = menu.get(i);
            ArrayList<Item> orderItems = order.getItems();
            orderItems.add(item);

            // Ask them to enter a new item index or q again, and take their input
            System.out.println("Please enter a menu item index or q to quit:");
            itemNumber = System.console().readLine();
        }
        // After you have collected their order, print the order details
        System.out.println(order.getName()+" "+"orders details:");
        
        for (Item item : order.getItems()){
            System.out.println(item.getName()+" "+item.getPrice());
        }
    	// as the example below. You may use the order's display method.
        
    }
}
