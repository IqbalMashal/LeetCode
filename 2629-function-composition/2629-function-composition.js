/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    // Return a function that takes 'x' as an input
    return function(x) {
        // Apply the functions from right to left (compose)
        return functions.reduceRight((acc, fn) => fn(acc), x);
    };
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */