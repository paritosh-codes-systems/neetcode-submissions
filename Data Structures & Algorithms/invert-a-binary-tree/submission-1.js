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
     * @return {TreeNode}
     */
    invertTree(root) {
        function flipTree(node) {
            if (!node) {
                return;
            }
            const temp = node.left;
            node.left = node.right
            node.right = temp;
            flipTree(node.left)
            flipTree(node.right);
        }
        flipTree(root);
        return root;
    }
}
