import java.util.ArrayList;
    
// Here we're creating a new data type called Order
public class Order {
    
    // MEMBER VARIABLES
    private String name; // default value of null
    private boolean ready; // default value false
    private ArrayList<Item> items = new ArrayList<Item>() ; // defaults to null

    // CONSTRUCTOR
    
    // No arguments, sets name to "Guest", initializes items as an empty list.
    
    public Order() {
        name="Guest";
        // ArrayList<Item> items = new ArrayList<Item>();
    }

    
    // OVERLOADED CONSTRUCTOR
    // Takes a name as an argument, sets name to this custom name.
    // Initializes items as an empty list.
    
    public Order(String name) {
        this.name = name;
    }
    
    // ORDER METHODS
    public void addItem(Item item){
        items.add(item);

    }

    public String getStatusMessage(){
        // Create a method called getStatusMessage that returns a String message. If the order is ready, return "Your order is ready.", if not, return "Thank you for waiting. Your order will be ready soon."
        if(ready){
            return "Your order is ready";
        }
        else{
            return "Thank you for waiting. Your order will be ready soon.";
        }
    }

    public double getOrderTotal(){
        double total = 0.0;
        for(Item i : this.items){
            total += i.getPrice() ;
        }
        return total;
    }

    public void display(){

        System.out.println("Customer Name: "+ this.name);
        for(Item i : this.items){
            System.out.println(i.getName() +" - - "+ i.getPrice());
        }
        System.out.println("Total : "+getOrderTotal());
        System.out.println();
    }

    // Most of your code will go here, 
    // so implement the getters and setters first!
    // GETTERS & SETTERS

    public String getName() {
        return name;
    }


    public void setName(String name) {
        this.name = name;
    }


    public boolean isReady() {
        return ready;
    }


    public void setReady(boolean ready) {
        this.ready = ready;
    }


    public ArrayList<Item> getItems() {
        return items;
    }


    public void setItems(ArrayList<Item> items) {
        this.items = items;
    }
    
    
}