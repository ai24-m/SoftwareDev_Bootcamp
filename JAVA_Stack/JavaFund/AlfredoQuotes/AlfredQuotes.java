import java.util.Date;
public class AlfredQuotes {
    
    public String basicGreeting() {
        // You do not need to code here, this is an example method
        return "Hello, lovely to see you. How are you?";
    }
    
    public String guestGreeting(String name) {
        // YOUR CODE HERE
        return String.format("hello, %s Lovely to see you.", name); 
    }
    
    public String dateAnnouncement() {
        // YOUR CODE HERE
        Date date = new Date();
        return "It is currently " + date ;
    }
    

    public String respondBeforeAlexis(String conversation)  {

        if(conversation.indexOf("Alexis") >= 0) {
            return "Right away, sir. She certainly isn't sophisticated enough for that.";
        }

        if (conversation.indexOf("Alfred") >= 0) {
            return "At your service. As you wish, naturally .";
        }

        return "Right. And with that I shall retire";
    }


    // public String respondBeforeAlexis(String conversation) {
    //     // YOUR CODE HERE
    //     // Write a method that accepts any string of conversation and responds appropriately.
    //     String conversation = "Welcome to Coding Dojo!";
    //     int a = ninja.indexOf("Coding"); // a is 11
    //     int b = ninja.indexOf("co"); // b is 3
    //     int c = ninja.indexOf("pizza"); // c is -1, "pizza" is not found


    //     return  ;
    // }
    
	// NINJA BONUS
	// See the specs to overload the guessGreeting method
    // SENSEI BONUS
    // Write your own AlfredQuote method using any of the String methods you have learned!
}

