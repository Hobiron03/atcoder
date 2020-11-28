def main():
    input()
    cards = list(map(int, input().split()))
    sorted_cards = sorted(cards, reverse=True)

    alice_point = 0
    bob_point = 0
    for i, card in enumerate(sorted_cards, 1):
        if i % 2 != 0:
            alice_point += card
        else:
            bob_point += card

    res = alice_point - bob_point
    print(res)


if __name__ == "__main__":
    main()
