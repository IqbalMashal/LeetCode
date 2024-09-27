/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    // Await the results of both promises
    const res1 = await promise1;
    const res2 = await promise2;
    
    // Return the sum of both resolved values
    return res1 + res2;
};

/**
 * Example usage:
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // Output: 4
 */
