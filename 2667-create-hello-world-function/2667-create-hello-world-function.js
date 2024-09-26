/**
 * @return {Function}
 */
var createHelloWorld = function() {
    let message = "Hello World"; 
    return function(...args) {
        return message;
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */