/**
 * @return {Function}
 */
var createHelloWorld = function() {

    return function(...argue){
        return "Hello World"
    }

};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */