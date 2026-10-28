class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        const cleanString = s.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
        const reversed = cleanString.split("").reverse().join("").toLowerCase();
        return cleanString === reversed;
    }
}
