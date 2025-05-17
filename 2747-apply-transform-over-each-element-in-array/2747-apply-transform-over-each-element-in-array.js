/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {

    trantransferArray = new Array(arr.length)
    for(let i = 0; i< arr.length; i++){
        trantransferArray[i] = fn(arr[i], i)
    }
    return trantransferArray
};