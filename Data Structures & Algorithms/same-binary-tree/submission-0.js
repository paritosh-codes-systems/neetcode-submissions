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
     * @param {TreeNode} p
     * @param {TreeNode} q
     * @return {boolean}
     */
    isSameTree(p, q) {
        let result = true;
        function isSameNode(n1, n2) {
            if (!n1 && n2) {
                result = false;
                return;
            }
            if (n1 && !n2) {
                result = false;
                return;
            }
            if (n1 && n2) {
                if (n1.val !== n2.val) {
                    result = false;
                return;
                }
                isSameNode(n1.left, n2.left);
                isSameNode(n1.right, n2.right);
            }
        }
        isSameNode(p, q);
        return result;
    }
}
