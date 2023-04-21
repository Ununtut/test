import random

print('This is my first project')
game = False
if input("do you want to play game? (yes/no)") == "yes":
    game = True

while game:
    nums = []
    for num in range(int(input("Haw many been nums?"))):
        nums.append(random.randint(1, 100))

    print(*nums)
    game = False
