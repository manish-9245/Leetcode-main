class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        bit_level = 1
        stack = [root] if root else []
        while stack:
            for i in range(len(stack)):
                if stack[i].val & 1 != bit_level: 
                    return False
                if i < len(stack) - 1 and ((stack[i].val > stack[i+1].val) == bool(bit_level) or stack[i].val == stack[i+1].val):
                    return False
            bit_level ^= 1
            stack = [node for n in stack for node in (n.left, n.right) if node]
        return True