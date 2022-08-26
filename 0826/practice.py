# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# # Node를 사용해서 트리 만들어보기
#
# # 2,3을 root의 왼쪽과 오른쪽에 추가
# root = Node('+')        #root노드 만들기
# root.left = Node('*')
# root.right = Node('E')
#
# # 4,5 번을 2번의 왼쪽과 오른 쪽에 추가
# root.left.left = Node('*')
# root.left.right = Node('D')
#
# root.left.left.left = Node('/')
# root.left.left.right = Node('C')
#
# root.left.left.left.left = Node('A')
# root.left.left.left.right = Node('B')
#
# # 전위순회 VLR
# def preorder(node):
#     if node:
#         print(node.data, end=" ")
#         preorder(node.left)
#         preorder(node.right)
#
#
# # 중위순회 LVR
# def inorder(node):
#     if node:
#         inorder(node.left)
#         print(node.data, end=" ")
#         inorder(node.right)
#
#
# # 후위순회
# def postorder(node):
#     if node:
#         postorder(node.left)
#         postorder(node.right)
#         print(node.data, end=" ")
#
#
#
# inorder(root)
# print()
# postorder(root)
# print()
# preorder(root)
# print()
#
# # 부모-자식 관의 관계로 표기된다.
# # 정점의 수 v가 주어진다
# v = int(input())
#
# tree = [Node(i) for i in range(v+1)]
# # v-1개의 간선이 나열된다.
# s = list(map(int, input().split()))
# # s를 순회하면서 2개씩 끊어서 tree의 정보에 저장한다.
# while s:
#     p = s.pop(0)
#     c = s.pop(0)
#
#     if tree[p].left:
#         tree[p].right = tree[c]
#     else:
#         tree[p].left = tree[c]

# print((3**28)*(4**4))

default = [1,2,3,45,6,7,8,5,3,2,1,5,1,5,7,8,6,5,6,8,99,1,2,3,45,6,7,8,9,0,0,2]
n = len(default)
for k in range(1, n+1, 20):
    print(*default[k:k+20])

