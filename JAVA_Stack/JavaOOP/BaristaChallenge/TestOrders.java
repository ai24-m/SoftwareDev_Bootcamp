import java.util.ArrayList;
public class TestOrders {

        public static void main(String[] args) {
        
        Item item1 = new Item("mocha",  3.2);
        Item item2 = new Item("latte", 2.3);
        Item item3 = new Item("drip coffee",  4.6);
        Item item4 = new Item("capuccino", 2.8);

        // Create 2 orders for unspecified guests (without specifying a name);

        Order order1 =new Order();
        Order order2 =new Order();

        // Create 3 orders using the overloaded constructor to give each a name for the order.

        Order order3 =new Order("Cindhuri");
        Order order4 =new Order("Jimmy");
        Order order5 =new Order("Noah");

        // Implement the addItem method within the Order class
        // Add at least 2 items to each of the orders using the addItem method you wrote, for example, to add item1 to order3 you would need to call the addItem method from the order3 instance like so: order3.addItem(item1);

        order1.addItem(item1);
        order1.addItem(item2);
        order2.addItem(item4);
        order2.addItem(item1);
        order3.addItem(item3);
        order3.addItem(item3);
        order4.addItem(item2);
        order4.addItem(item2);
        order5.addItem(item2);
        order5.addItem(item1);

        // Implement the getStatusMessage method within the Order class
        // Test your getStatusMessage functionality by setting some orders to ready and printing the messages for each order. For example: order2.setReady(true); System.out.println(order2.getStatusMessage());
        
        System.out.println("_____Order Status of order 1  _____ \n ");
        System.out.println(order1.getStatusMessage());
        
        order1.setReady(true);
        System.out.println(order1.getStatusMessage()+"\n");
        
        System.out.println("_____Order Status of order 4 _____ \n ");
        System.out.println(order4.getStatusMessage());
        
        order4.setReady(true);
        System.out.println(order4.getStatusMessage()+"\n");
        System.out.println("\n");
        
        // Implement the getOrderTotal method within the Order class
        // Test the total by printing the return value like so: System.out.println(order1.getOrderTotal());
        System.out.println("------- total of order 1 ------- \n ");
        System.out.println(order1.getOrderTotal());
        System.out.println("------- total of order 2 ------- \n ");
        System.out.println(order2.getOrderTotal());
        System.out.println("------- total of order 3 -------\n ");
        System.out.println(order3.getOrderTotal());
        

        // Implement the display method within the Order class
        // Finally, call the display method on all of your orders, like so: order3.display();
        System.out.println("_____ All Orders _____");
        order1.display();
        order2.display();
        order3.display();
        order4.display();
        order5.display();
        
        }
}

