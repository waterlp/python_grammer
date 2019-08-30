from collections import deque

def serialize(self, root):
    res = []
    def preOrder(root):
        if not root:
            res.append('#')
        else:
            res.append(str(root.val))
            preOrder(root.left)
            preOrder(root.right)

    preOrder(root)
    return ' '.join(res)


def deserialize(self, data):
    tmp = deque(i for i in data.split())

    def buildBT():
        val = tmp.popleft()
        if val == '#':
            return None
        else:
            root = TreeNode(int(root.val))
            root.left = buildBT()
            root.right = buildBT()

    return buildBT()

