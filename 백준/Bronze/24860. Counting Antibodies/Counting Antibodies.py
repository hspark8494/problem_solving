A1, A2 = map(int, input().split(" "))
B1, B2 = map(int, input().split(" "))
X1, X2, X3 = map(int, input().split(" "))
X = X1*X2*X3
print(A1*A2*X + B1*B2*X)