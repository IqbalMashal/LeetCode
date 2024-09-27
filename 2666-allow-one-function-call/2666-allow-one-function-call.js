/**
 * @param {Function} fn
 * @return {Function}
 */
 
var once = function(fn) {
    let called = false; // A flag to track if the function has been called
    return function(...args) {
        if (!called) { // If the function hasn't been called yet
            called = true; // Set the flag to true
            return fn(...args); // Call the function with the arguments
        }
        return undefined; // Return undefined if the function has already been called
    };
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
