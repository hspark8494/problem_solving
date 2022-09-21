from sys import stdin
input = stdin.readline

root = {}

for _ in range(int(input())):
    node = input().rstrip().split(" ")
    curr = root
    for n in node[1:]:
        if n not in curr:
            curr[n] = {}
        curr = curr[n]

def print_nodes(node:dict, dept, name):
    if name:
        print("-"*dept+name)
    for key in sorted(node.keys()):
        print_nodes(node[key], dept+2, key)

print_nodes(root, -2, "")