class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const numLength = nums.length;
        for (let i = 0; i < numLength; i++) {
            for (let j = 0; j < numLength; j++) {
                if (i === j) {
                    continue;
                }
                if (nums[i] + nums[j] === target) {
                    return [i, j];
                }
            }
        }
    }
}
