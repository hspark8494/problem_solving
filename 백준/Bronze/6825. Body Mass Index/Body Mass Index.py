W, H = float(input()), float(input())
B = W/(H*H)
if B > 25:
    print('Overweight')
elif B >= 18.5:
    print("Normal weight")
else:
    print("Underweight")