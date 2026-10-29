class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        const length = prices.length;
        let highestProfit = 0;
        for (let i = 0; i < length; i++) {
            for (let j = i + 1; j < length; j++) {
                const profit = prices[j] - prices[i];
                highestProfit = Math.max(highestProfit, profit);
            }
        }
        return highestProfit;
    }
}
