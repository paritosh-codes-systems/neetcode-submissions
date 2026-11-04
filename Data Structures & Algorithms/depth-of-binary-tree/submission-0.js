/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    maxDepth(root) {
        let max = 0;
        function getCount(node, count = 1) {
            if (!node) {
                return;
            }
            max = Math.max(max, count);
            if (node.left) {
                getCount(node.left, count + 1)
            }
            if (node.right) {
                getCount(node.right, count + 1);
            }
            return;
        }
        getCount(root);
        return max;
    }
}
