A, B = input().split()

mx = int(A.replace('5', '6')) + int(B.replace('5', '6'))
mn = int(A.replace('6', '5')) + int(B.replace('6', '5'))

print(int(mn), int(mx))
