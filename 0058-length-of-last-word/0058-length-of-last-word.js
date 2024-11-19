/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {

    let ans = 0;

    if(s.length == 1){
        return 1;
    }

  let arr = s.trim().split(' ');
  let size = arr.length -1;

  for(let i = 0; i < arr[size].length; i++){

    ans++;

  }

    return ans;
};