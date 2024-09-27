/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
 
var reduce = function(nums, fn, init) {
    let val = init; // Initialize val to the provided initial value

    // Iterate through the array
    for (let i = 0; i < nums.length; i++) {
        val = fn(val, nums[i]); // Update val with the result of applying fn
    }

    return val; // Return the accumulated value
};