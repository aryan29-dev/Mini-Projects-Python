import random
from collections import Counter

RANKS = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
SUITS = ["Spade", "Heart", "Club", "Diamond"]

RANK_VALUE = {r:i for i,r in enumerate(RANKS, start=2)}  # 2..14

HAND_NAME = {
    8: "Straight Flush",
    7: "Four of a Kind",
    6: "Full House",
    5: "Flush",
    4: "Straight",
    3: "Three of a Kind",
    2: "Two Pair",
    1: "One Pair",
    0: "High Card"
}

def new_deck():
    deck = [f"{suit} {rank}" for suit in SUITS for rank in RANKS]
    random.shuffle(deck)
    return deck

def parse_card(card_str: str):
    suit, rank = card_str.split(" ", 1)
    return suit, rank

def straight_high(values):
    uniq = sorted(set(values))
    if 14 in uniq:
        uniq.insert(0, 1)
    best = None
    run = 1
    for i in range(1, len(uniq)):
        if uniq[i] == uniq[i-1] + 1:
            run += 1
            if run >= 5:
                best = uniq[i]
        else:
            run = 1
    return best

def evaluate_5(cards5):
    suits = [parse_card(c)[0] for c in cards5]
    ranks = [parse_card(c)[1] for c in cards5]
    values = sorted([RANK_VALUE[r] for r in ranks], reverse=True)

    is_flush = len(set(suits)) == 1
    s_high = straight_high(values)
    is_straight = s_high is not None

    counts = Counter(values)
    groups = sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True)
    counts_sorted = sorted(counts.values(), reverse=True)

    # Straight Flush
    if is_flush and is_straight:
        return (8, (s_high,))

    # Four of a Kind
    if counts_sorted == [4,1]:
        quad = groups[0][0]
        kicker = max(v for v in values if v != quad)
        return (7, (quad, kicker))

    # Full House
    if counts_sorted == [3,2]:
        trip = groups[0][0]
        pair = groups[1][0]
        return (6, (trip, pair))

    # Flush
    if is_flush:
        return (5, tuple(values))

    # Straight
    if is_straight:
        return (4, (s_high,))

    # Three of a Kind
    if counts_sorted == [3,1,1]:
        trip = groups[0][0]
        kickers = sorted([v for v in values if v != trip], reverse=True)
        return (3, (trip, *kickers))

    # Two Pair
    if counts_sorted == [2,2,1]:
        pair1 = groups[0][0]
        pair2 = groups[1][0]
        kicker = max(v for v in values if v not in (pair1, pair2))
        hi, lo = max(pair1, pair2), min(pair1, pair2)
        return (2, (hi, lo, kicker))

    # One Pair
    if counts_sorted == [2,1,1,1]:
        pair = groups[0][0]
        kickers = sorted([v for v in values if v != pair], reverse=True)
        return (1, (pair, *kickers))

    # High Card
    return (0, tuple(values))

def best_hand_7(cards7):
    best_score = None
    best5 = None
    n = len(cards7)
    for a in range(n):
        for b in range(a+1, n):
            for c in range(b+1, n):
                for d in range(c+1, n):
                    for e in range(d+1, n):
                        combo = [cards7[a], cards7[b], cards7[c], cards7[d], cards7[e]]
                        score = evaluate_5(combo)
                        if best_score is None or score > best_score:
                            best_score = score
                            best5 = combo
    return best_score, best5

def show_cards(label, cards):
    print(label)
    for c in cards:
        print("\t", c)

print("Welcome to the POKER game application")
print("Commands: deal, draw, show, result, quit")

deck = []
dealer_cards = []
user_cards = []
board = []

while True:
    cmd = input("> ").strip().lower()

    if cmd == "deal":
        deck = new_deck()
        board = []
        user_cards = [deck.pop(), deck.pop()]
        dealer_cards = [deck.pop(), deck.pop()]
        print("Cards shuffled and ready")
        show_cards("User cards:", user_cards)

    elif cmd == "draw":
        if not deck:
            print("You need to type 'deal' first.")
            continue
        if board:
            print("Shared cards already drawn. Type 'deal' to start a new round.")
            continue
        board = [deck.pop() for _ in range(5)]
        show_cards("Shared cards:", board)

    elif cmd == "show":
        if not dealer_cards:
            print("You need to type 'deal' first.")
            continue
        show_cards("Dealer cards:", dealer_cards)

    elif cmd == "result":
        if not (user_cards and dealer_cards and board):
            print("Run 'deal' then 'draw' first (and 'show' if you want to see dealer).")
            continue

        user7 = user_cards + board
        dealer7 = dealer_cards + board

        user_score, user_best5 = best_hand_7(user7)
        dealer_score, dealer_best5 = best_hand_7(dealer7)

        show_cards("Your best 5:", user_best5)
        print("Your hand:", HAND_NAME[user_score[0]])

        show_cards("Dealer best 5:", dealer_best5)
        print("Dealer hand:", HAND_NAME[dealer_score[0]])

        if user_score > dealer_score:
            print("\n You WIN!")
        elif user_score < dealer_score:
            print("\n Dealer wins.")
        else:
            print("\n Tie!")

    elif cmd == "quit":
        print("Thank you for playing.")
        break

    else:
        print(f"Command [{cmd}] not found.")