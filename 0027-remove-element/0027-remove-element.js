/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === val) {
            nums.splice(i, 1); // Remove the element at index i
            i--; // Decrement i because the array has been shortened
        }
    }
    return nums.length; // Return the modified length of the array
};
