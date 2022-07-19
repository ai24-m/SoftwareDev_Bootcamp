public class Item {
    
    // MEMBER VARIABLES
    private String name;
    private double price;
    
    // CONSTRUCTOR
    //   Takes a name and price as arguments 

    public Item(String name, double price) {

        //   and sets them accordingly

        this.name = name;
        this.price = price;
    }

    // GETTERS & SETTERS  - for name and price

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

}