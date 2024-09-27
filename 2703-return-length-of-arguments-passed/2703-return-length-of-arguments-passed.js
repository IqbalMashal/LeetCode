/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {

    let counter = 0;
    if(args.length === 0 ){
        return 0;
    }

    for (let i = 0; i < args.length; ++i){
        counter++;
    }

    return counter;
    
};

/**
 * argumentsLength(1, 2, 3); // 3
 */