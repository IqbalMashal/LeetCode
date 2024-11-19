/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    if (needle === "") {
        return -1;
    }
    
    // Use indexOf to find the first occurrence of needle in haystack
    let ans = haystack.indexOf(needle);
    
    // Return the result
    return ans;
    
};