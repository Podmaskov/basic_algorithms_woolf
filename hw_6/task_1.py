class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def find_max_value(root):
    """
    Знаходить найбільше значення у двійковому дереві пошуку (або AVL-дереві).
    Приймає корінь дерева та повертає максимальний key.
    """
    if root is None:
        return None

    current = root
    # В двійковому дереві пошуку найбільше значення знаходиться у правому піддереві
    while current.right is not None:
        current = current.right
    return current.key

# Приклад використання:
if __name__ == "__main__":
    node8 = TreeNode(8)
    node10 = TreeNode(10, left=node8)
    node17 = TreeNode(17)
    node25 = TreeNode(25)
    node20 = TreeNode(20, left=node17, right=node25)
    root = TreeNode(15, left=node10, right=node20)

    max_value = find_max_value(root)
    print("Найбільше значення в дереві:", max_value)