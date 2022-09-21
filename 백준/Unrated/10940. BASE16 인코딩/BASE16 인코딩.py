import base64
print(str(base64.b16encode(input().encode("UTF-8")))[2:-1])