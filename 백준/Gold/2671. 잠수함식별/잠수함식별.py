import re
print("SUBMARINE" if re.fullmatch("(100+1+|01)+", input()) else "NOISE")