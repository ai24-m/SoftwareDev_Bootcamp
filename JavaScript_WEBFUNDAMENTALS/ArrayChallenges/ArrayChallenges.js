/* Always Hungry
Write a function that is given an array and each time the value is "food" it should console log "yummy". If "food" was not present in the array console log "I'm hungry" once.
High Pass Filter
Given an array and a value cutoff, return a new array containing only the values larger than cutoff.
Better than average
Given an array of numbers return a count of how many of the numbers are larger than the average.
Array Reverse
Write a function that will reverse the values an array and return them.
Fibonacci Array
Fibonacci numbers have been studied for years and appear often in nature. Write a function that will return an array of Fibonacci numbers up to a given length n. Fibonacci numbers are calculated by adding the last two values in the sequence together. So if the 4th value is 2 and the 5th value is 3 then the next value in the sequence is 5.
*/ 


// Always Hungry
arr1= [3.14, "food", "pie", true, "food"];
arr2= [4, 1, 5, 7, 2];
function alwaysHungry(arr) {
    var out;            
    for(var i=0 ; i<arr.length ; i++){
        if(arr[i]=="food"){   
            out="yummy"; 
            console.log(out);      
        }
        else{
            out ="I'm hungry";
            a= out;
        }
    }return a;
}
alwaysHungry(arr1);
console.log(alwaysHungry(arr2));


// High Pass Filter
function highPass(arr, cutoff) {
    var filteredArr = [];
    for(i=0 ; i<arr.length ; i++){
        if(arr[i] > cutoff){
            filteredArr.push (arr[i])
        }
    }return filteredArr;
}


var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result); 


//Better than average
function betterThanAverage(arr) {
    var sum = 0;
    for(i=0 ; i<arr.length ; i++){
        sum = sum+arr[i];
    }
    average = sum/i;
    var count = 0
    for(i=0 ; i<arr.length ; i++){
        if(arr[i]> average){
            count=count+1;
        }
    }
    // console.log(average)
    // console.log(sum)
    return count;
}
console.log("Better than average");
var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result); // we expect back 4


//Array Reverse
function reverse(arr) {
    var newarr=[];
    for(var i= arr.length-1 ; i>=0 ; i--){
        newarr.push(arr[i]);
    }return newarr;
}
console.log("Array Reverse");
var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result); // we expect back ["e", "d", "c", "b", "a"]


//Fibonacci Array
function fibonacciArray(n) {
    // the [0, 1] are the starting values of the array to calculate the rest from
    var fibArr = [0, 1];
    while (n > 0){
        temp = fibArr[0];
        fibArr[0] = fibArr[0] + fibArr[1];
        fibArr[1] = temp;
        n--;
        console.log(temp)
        }
    return temp;
}
    
var result = fibonacciArray(10);
console.log(result); // we expect back [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


