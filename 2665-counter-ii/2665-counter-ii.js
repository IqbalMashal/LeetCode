/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let initialValue = init; // Store the initial value for reset
    
    return {
        increment: function() {
            init++; // Increment `init` first
            return init; // Return the incremented value
        },
        reset: function() {
            init = initialValue; // Reset `init` to the initial value
            return init;
        },
        decrement: function() {
            init--; // Decrement `init` first
            return init; // Return the decremented value
        }
    };
};


/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
