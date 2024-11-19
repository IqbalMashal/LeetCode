/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {

    a = digits.join('');
    a = BigInt(a);
    a++;

    a = a.toString().split('').map(Number);
    return a;
    
};