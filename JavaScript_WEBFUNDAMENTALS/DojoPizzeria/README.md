### Dojo Pizzeria
**Objectives**
* Practice making JavaScript objects
* Practice using Math.random()
## A Sandwich Factory
In this assignment we'll be making pizzas in JavaScript! And if we're going to just make one pizza we can define it all at once like the sandwich we see below.
``` 
var sandwich = {
    bread:    "sourdough",
    protein:  "london broil",
    cheese:   "lacey swiss cheese",
    toppings: ["romaine lettuce", "heirloom tomatoes", "horseradish sauce"]
};
    
console.log(sandwich);
```

But what if we wanted to make multiple sandwiches? We could define a function that allows us to craft a sandwich!
``` 
function sandwichFactory(bread, protein, cheese, toppings) {
    var sandwich = {};
    sandwich.bread = bread;
    sandwich.protein = protein;
    sandwich.cheese = cheese;
    sandwich.toppings = toppings;
    return sandwich;
}
    
var s1 = sandwichFactory("wheat", "turkey", "provolone", ["mustard", "fried onions", "arugula"]);
console.log(s1);
```

## The Pizza Oven
Create a function called **pizzaOven**. We should feel free to customize what information we keep track of for our pizza, but let's make sure that we include the following: crustType, sauceType, cheeses, and toppings.

Create a function called pizzaOven that returns a JavaScript (Pizza) Object

Create a pizza with: "deep dish", "traditional", ["mozzarella"], and ["pepperoni", "sausage"]

Create a pizza with: "hand tossed", "marinara", ["mozzarella", "feta"], and ["mushrooms", "olives", "onions"]

Create 2 more pizzas with any toppings we like!

**Bonus Challenge:** Create a function called **randomPizza** that uses Math.random() to create a random pizza!