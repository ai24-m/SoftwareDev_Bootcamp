// Methods of the String class

// - Length - Strings have a method to determine their length.

public class StringDemo {
     public static void main(String[] args) {
        String ninja = "Coding Dojo is Awesome!";
        int length = ninja.length();
        System.out.println( "String Length is : " + length );
     }
}

// This will result in: String Length is: 23

// - Concatenate: A String method that allows two strings to be squashed together. Since each string is immutable, this results in a brand new string.

String string1 = "My name is ";
String string2 = "Michael";
String string3 = string1.concat(string2);
System.out.println(string3);
// will output My name is Michael



// - Format: Another way of concatenating strings!

String ninja = String.format("Hi %s, you owe me $%.2f !", "Jack", 25.0);
System.out.println(ninja);
// Will print out Hi Jack, you owe me $25.00 !
// Where %s is expecting a string
// And %.2f is expecting a float data type. The value 2 will just place two values to right of the decimal point.

// - IndexOf: The indexOf method searches left-to-right inside the given string for a "target" string. The indexOf() method returns the index number where the target string is first found or -1 if the target is not found. 

String ninja = "Welcome to Coding Dojo!";
int a = ninja.indexOf("Coding"); // a is 11
int b = ninja.indexOf("co"); // b is 3
int c = ninja.indexOf("pizza"); // c is -1, "pizza" is not found


// Trim: The trim() method removes any trailing or leading white spaces from the string.

String sentence = "   spaces everywhere!   ";
System.out.println(sentence.trim())

// This will output: spaces everywhere!.


// - Uppercase and Lowercase: The String class provides methods to lowercase and uppercase strings.


String a = "HELLO";
String b = "world";
System.out.println(a.toLowerCase()); // hello
System.out.println(b.toUpperCase()); // WORLD


// Equality: We can compare the equality of a string in two ways. Do they refer to the exact same object, or do they have the same exact sequence of characters.

// Normal string assignment
String a = "same string";
String b = "same string";
System.out.println(a == b); // true
// Creating new strings as separate objects (another way to create a String)
a = new String("same letters");
b = new String("same letters");
System.out.println(a == b); // false. Not the same object in memory.
System.out.println(a.equals(b)); // true. same exact characters.

//When to use == and when to use .equals()

/* When we use == in Java with objects, we are comparing if both variables point to the same address and the same object in memory. Much of the time this will have the desired outcome, but from time to time we might encounter some behavior that will seem different from what we've seen in other programming languages. For the the assignments in this chapter, it will be fine just to use == to compare our basic built in types. However, later as you work with more object types, you will often need to use .equals() instead of  == to accomplish the desired comparison. In fact, when dealing with objects, this is convention.  */

String a = new String( "Dojo" );
System.out.println( a == "Dojo" );
// surprisingly this will print out `false`

// We can still check if the two variables have the same value,  we just need to use .equals() instead.

String a = new String( "Dojo" );
System.out.println( a.equals("Dojo") );
// this actually will print out `true`


