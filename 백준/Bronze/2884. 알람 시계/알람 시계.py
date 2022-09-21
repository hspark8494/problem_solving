a,b = map(int, input().split())
c = a*60+b-45

print(str(int(c/60%24)) + " " + str((c%60)))