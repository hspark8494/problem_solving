d = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5'}
def f(x): return x if x not in d else d[x]

print(''.join(map(f, list(input()))))
