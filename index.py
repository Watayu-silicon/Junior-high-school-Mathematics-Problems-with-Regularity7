num = int(input())
white = 1
black = 0
for i in range(1, num):
    if i%2 == 1:
        black += 8 * i
    elif i%2 == 0:
        white += 8 * i
print('白い石:', white)
print('黒い石', black)