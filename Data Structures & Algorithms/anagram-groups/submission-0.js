class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    sortString(str) {
        return str.split('').sort().join('');
    }
    groupAnagrams(strs) {
        const length = strs.length;
        const result = [];
        let anagramMap = new Map();
        for (let i = 0; i < length; i++) {
            const sorted = this.sortString(strs[i]);
            const value = anagramMap.get(sorted) || [];
            anagramMap.set(sorted, [...value, strs[i]]);
        }
        anagramMap.forEach((value) => result.push(value));
        return result;
    }
}
