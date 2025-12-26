import random

def roll(dice, sel):
    if sel is None:
        for i in range(5):
            dice.append(random.randint(1, 6))
    else:
        for i in range(5):
            if sel[i] == 0:
                dice[i] = random.randint(1, 6)

def play():
    s = None
    d = []
    i = 1
    while True:
        roll(d, s)
        if i == 1:
            print("First", end='')
        elif i == 2:
            print("Second", end='')
        else:
            print("Final", end='')
        print(" roll:", *d)
        if i < 3:
            i += 1
            s = [int(x) for x in input("Roll again? [0 to roll, 1 to keep, a single 1 to keep all] ").strip().split(" ")]
            if len(s) == 1:
                break
        else:
            break
    d.sort()
    return d


def is_yahtzee(dice):
    return dice[0] == dice[1] == dice[2] == dice[3] == dice[4]


def is_large_straight(dice):
    return dice == [1, 2, 3, 4, 5] or dice == [2, 3, 4, 5, 6]


def is_sublist(my_list, sub_list):
    return sub_list == [x for x in sub_list if x in my_list]


def is_small_straight(dice):
    return is_sublist(dice, [1, 2, 3, 4]) or is_sublist(dice, [2, 3, 4, 5]) or is_sublist(dice, [3, 4, 5, 6])


def is_full_house(dice):
    return (dice[0] == dice[1]) and (dice[3] == dice[4]) and (dice[2] == dice[0] or dice[2] == dice[3])


def is_four_of_a_kind(dice):
    return dice[0] == dice[1] == dice[2] == dice[3] or \
           dice[1] == dice[2] == dice[3] == dice[4]


def is_three_of_a_kind(dice):
    return dice[0] == dice[1] == dice[2] or \
           dice[1] == dice[2] == dice[3] or \
           dice[2] == dice[3] == dice[4]


score = 0
round_number = 0
print("Welcome to Mini Yahtzee!")
while True:
    d = play()
    if is_yahtzee(d):
        print("YAHTZEE!")
        score += 50
    elif is_large_straight(d):
        print("LARGE STRAIGHT")
        score += 40
    elif is_small_straight(d):
        print("SMALL STRAIGHT")
        score += 30
    elif is_full_house(d):
        print("FULL HOUSE!")
        score += 25
    elif is_four_of_a_kind(d):
        print("FOUR OF A KIND")
        score += sum(d)
    elif is_three_of_a_kind(d):
        print("THREE OF A KIND")
        score += sum(d)
    else:
        print("CHANCE")
        score += sum(d)

    round_number += 1
    print("Round:", round_number, "Score:", score)
    n = input("Play again? [q to quit, any other key to continue] ")
    if n.lower() == "q":
        print("Thank you for playing Mini Yahtzee!")
        break
