class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const numLength = nums.length;
        const numSet = new Set([...nums]);
        if (numSet.size !== numLength) {
            return true
        }
        return false;
    }
}
