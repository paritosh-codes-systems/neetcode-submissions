/**
 * Pair class to store key-value pairs
 */
// class Pair {
//     /**
//      * @param {number} key The key to be stored in the pair
//      * @param {string} value The value to be stored in the pair
//      */
//     constructor(key, value) {
//         this.key = key;
//         this.value = value;
//     }
// }
class Solution {
    /**
     * @param {Pair[]} pairs
     * @returns {Pair[][]}
     */
    insertionSort(pairs) {
        const length = pairs.length;
        let result = [];
        for (let i = 0; i < length; i++) {
            let j = i - 1;
            while (j >= 0 && pairs[j].key > pairs[j + 1].key) {
                const temp = pairs[j];
                pairs[j] = pairs[j + 1];
                pairs[j + 1] = temp;
                j--;
            }
            result.push([...pairs]);
        }
        return result;
    }
}
