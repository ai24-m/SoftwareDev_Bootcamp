public class coffeTest {
    public static void main(String[] args) {
         //inisializing CoffeeKiosk object

        CoffeeKiosk coffeKiosk = new CoffeeKiosk();
        coffeKiosk.addMenuItem("Banana", 2.00);
        coffeKiosk.addMenuItem("Coffe", 1.50);
        coffeKiosk.addMenuItem("Latte", 4.50);
        coffeKiosk.addMenuItem("Capuccino", 3.00);
        coffeKiosk.addMenuItem("Muffin", 4.00);
        // coffeKiosk.displayMenu();
        coffeKiosk.newOrder();
    }
}
