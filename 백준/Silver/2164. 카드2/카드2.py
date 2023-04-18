import sys
from collections import deque
N = int(input())
def cardDeck2(N):
    cards = deque(maxlen=N+1)
    for i in range(N):
        cards.append(i+1)
    while not len(cards) == 1:
        cards.popleft()
        a = cards.popleft()
        cards.append(a)
    print(cards[0])
cardDeck2(N)