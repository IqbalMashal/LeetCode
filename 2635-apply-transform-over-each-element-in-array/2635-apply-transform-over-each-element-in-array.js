/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {

    let result = []; // Create an empty array to store results
    
    // Iterate through each element in the input array
    for (let i = 0; i < arr.length; i++) {
        result[i] = fn(arr[i], i); // Apply the function to each element and store in result
    }
    return result;
    
};