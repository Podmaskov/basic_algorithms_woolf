class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def find_min_value(root):
    """
    Знаходить найменше значення у двійковому дереві пошуку (або AVL-дереві).
    Приймає корінь дерева та повертає мінімальний key.
    """
    if root is None:
        return None

    current = root
    # В двійковому дереві пошуку найменше значення знаходиться у лівому піддереві
    while current.left is not None:
        current = current.left
    return current.key

# Приклад використання:
if __name__ == "__main__":

    node8 = TreeNode(8)
    node10 = TreeNode(10, left=node8)
    node17 = TreeNode(17)
    node25 = TreeNode(25)
    node20 = TreeNode(20, left=node17, right=node25)
    root = TreeNode(15, left=node10, right=node20)

    min_value = find_min_value(root)
    print("Найменше значення в дереві:", min_value)