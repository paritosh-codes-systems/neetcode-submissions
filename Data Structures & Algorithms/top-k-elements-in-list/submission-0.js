class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const totalMap = new Map();
        let result = [];
        for (let i = 0; i < nums.length; i++) {
            const value = totalMap.get(nums[i]) || 0;
            totalMap.set(nums[i], value + 1);
        }
        const allEntries = [...totalMap.entries()].sort((a, b) => {
            if (a[1] < b[1]) {
                return 1;
            }
            if (a[1] > b[1]) {
                return -1
            }
            return 0;
        });
        for (let i = 0; i < k; i++) {
            result.push(allEntries[i][0]);
        }
        return result;
    }
}
