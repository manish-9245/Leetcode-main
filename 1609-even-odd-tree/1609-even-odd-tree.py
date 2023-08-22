class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        level = 0
        while queue:
            prev_val = None
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop(0)
                val = node.val
                if (level % 2 == 0 and (val % 2 == 0 or (prev_val is not None and val <= prev_val))) or \
                   (level % 2 == 1 and (val % 2 == 1 or (prev_val is not None and val >= prev_val))):
                    return False
                prev_val = val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return True