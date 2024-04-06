import random

dice_art = {
    1: (
        "┌───────┐",
        "│       │",
        "│   ●   │",
        "│       │",
        "└───────┘",
    ),
    2: (
        "┌───────┐",
        "│ ●     │",
        "│       │",
        "│     ● │",
        "└───────┘",
    ),
    3: (
        "┌───────┐",
        "│ ●     │",
        "│   ●   │",
        "│     ● │",
        "└───────┘",
    ),
    4: (
        "┌───────┐",
        "│ ●   ● │",
        "│       │",
        "│ ●   ● │",
        "└───────┘",
    ),
    5: (
        "┌───────┐",
        "│ ●   ● │",
        "│   ●   │",
        "│ ●   ● │",
        "└───────┘",
    ),
    6: (
        "┌───────┐", # 0
        "│ ●   ● │", # 1
        "│ ●   ● │", # 2
        "│ ●   ● │", # 3
        "└───────┘", # 4
    ),
}

#輸入問要投幾次骰子

num_dice = int(input("請輸入你想要投擲幾次骰子"))
dice = [ ] #用來存投出骰子後的數字

#骰子點數怎麼決定
#random

for i in range(num_dice): #投擲幾次
    dice_number = random.randint(1,6) #每一次投擲骰子都會是1~6
    dice.append(dice_number) #存進去dice list 裡面


#怎麼把骰子點數印出來
#寫一個通用的方法
def get_dice_number(number):
    for i in range(5):
        print(dice_art.get(number)[i]) #get方法是拿到key 然後把key中的五個tuple印出來。

#用通用的方法印出骰子

for i in dice:
    get_dice_number(i) #如果是2 就會印出第二個骰子（key 2) 

print("骰子總點數：",sum (dice))

