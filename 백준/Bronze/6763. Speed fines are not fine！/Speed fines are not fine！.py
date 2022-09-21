import sys

input = sys.stdin.readline

x = -int(input()) + int(input())

if x<=0:
    print("Congratulations, you are within the speed limit!")
else:
    result = 500
    if x<=20:
        result = 100
    elif x<=30:
        result = 270
    print(f"You are speeding and your fine is ${result}.")