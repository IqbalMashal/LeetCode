/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
       if (word1.length == 0) {
        return word1;
    } else if (word2.length == 0) {
        return word2;
    }
    let res = [];
    let size = word1.length + word2.length;
    let str1Index = 0;
    let str2Index = 0;

    // Iterate over the combined length of both strings
    for (let i = 0; i < size; i++) {
        if (i % 2 == 0) {
            if (str1Index < word1.length) {
                res[i] = word1[str1Index];
                str1Index++;
            } else {
                res[i] = word2[str2Index];
                str2Index++;
            }
        } else {
            if (str2Index < word2.length) {
                res[i] = word2[str2Index];
                str2Index++;
            } else {
                res[i] = word1[str1Index];
                str1Index++;
            }
        }
    }
    return res.join('');
 
};