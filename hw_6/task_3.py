class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def sum_tree(root):
    """
    Рекурсивно обчислює суму всіх значень у двійковому дереві пошуку (або AVL-дереві).
    Якщо дерево порожнє, повертає 0.
    """
    if root is None:
        return 0
    return root.key + sum_tree(root.left) + sum_tree(root.right)

# Приклад використання:
if __name__ == "__main__":
    node8 = TreeNode(8)
    node10 = TreeNode(10, left=node8)
    node17 = TreeNode(17)
    node25 = TreeNode(25)
    node20 = TreeNode(20, left=node17, right=node25)
    root = TreeNode(15, left=node10, right=node20)

    total_sum = sum_tree(root)
    print("Сума всіх значень в дереві:", total_sum)