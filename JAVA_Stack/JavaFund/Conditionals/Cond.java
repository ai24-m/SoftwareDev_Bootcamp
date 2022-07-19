


// If Statements ________________

if (condition) {
    // what to do if condition is true
}
// continue with program
boolean isRaining = true;
    
if(isRaining) {
    System.out.println("Bring an umbrella.");
}


// If-Else Chains _________________

if(condition) {
    // what to do if condition is true
}
else if(2nd condition) {        
    // what to do if 2nd condition is true
}
// ... can have 0 to many else-if statements ...
else {                           
    // what to do if none of the previous conditions are met
} // can have 1 or no else statement

// If / Else Statements _______________

boolean isRaining = true;
    
if(isRaining) {
    System.out.println("Bring an umbrella.");
}
else {
    System.out.println("Have fun!");
}

// If /Else If / Else Statements _____________

boolean isRaining = true;
boolean isCold = true;
    
if(isRaining) {
    System.out.println("Bring an umbrella.");
}
else if(isCold) {
    System.out.println("Wear a coat.");
}
else {
    System.out.println("Have fun!");
}



// Comparison Operators ___________

// == equal
int count = 1; // assigns a value
count == 1; // evaluates to true
count == 2; // evaluates to false

// != 	not equal 
count != 2; // true
count != 1; // false

// 	> greater than
count > 2; // false
count > 0; //  true

// < less than 

count < 2;  // true
count < 1;  // false

// >= greater than or equal to
count >= 2; // false;
count >= 1; // true

// <= less than or equal to
count <= 2; // true;
count <= 1; // true



// Logical Operators ______

// &&  AND - Both conditions must be true to be true -----
int age = 45;
    
age < 65 && age > 17; 
// evaluates to true
//(Would pay adult price)
    
age < 110 && age > 65; 
// false
// (Is not a senior, nor immortal)


// || OR - One of the conditions must be true ------
int age = 77;
age < 10 || age > 65;
// true
// (Doesn't care what people think!)


// !  NOT -----
int age = 16;
!(age < 16)
// true
// (May obtain a drivers license)