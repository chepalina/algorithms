import random
from dataclasses import dataclass
from enum import Enum
from itertools import product
from typing import Type


class Suit(Enum):
    a = "a"


class CardType(Enum):
    six = 6
    jack = 10


@dataclass
class Card:
    suit: Suit
    type: CardType


@dataclass
class Deck:

    cards: list[Card]
    suits: Suit
    types: CardType

    def __post_init__(self):
        self._card_type: Type[Card] = Card

    def __len__(self):
        return len(self.cards)

    def reset(self):
        self.cards = self._make()
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def get_next(self):
        return self.cards.pop()

    def is_empty(self):
        return bool(self.cards)

    def _make(self):
        return [
            self._card_type(s, t)
            for t, s in list(
                product([v for v in type(self.types)], [s for s in type(self.suits)])
            )
        ]


@dataclass
class BlackJackCard(Card):

    suit: Suit
    type: CardType

    def get_points(self) -> int:
        return self.type.value


@dataclass
class BlackJack(Deck):

    deck_num: int
    shoe: int

    def __post_init__(self):
        self._card_type: Type[BlackJackCard] = BlackJackCard

    def reset(self):
        cards = self._make()
        for _ in range(self.deck_num):
            self.cards.extend(cards.copy())
        self.shuffle()

    def put_shoe(self):
        self.shoe = random.randint(len(self) // 2, len(self))


# --------------Recommended--------------------


class SuitR(Enum):
    club = "club"
    diamond = "diamond"
    heart = "heart"
    spade = "spade"


class CardR:
    def __init__(self, face_value, suit):
        self._available = True
        self.face_value = face_value
        self.suit = suit

    def value(self) -> int:
        pass

    def is_available(self):
        return self._available


class DeckR:

    def __init__(self):
        self.cards: list[CardR] = []
        self.dealt_index = 0

    def set(self):
        pass

    def shuffle(self):
        pass

    def remaining(self):
        return len(self.cards) - self.dealt_index

    def deal_hand(self, number: int) -> list[CardR]:
        pass

    def deal(self) -> CardR:
        pass


class Hand:

    def __init__(self):
        self._cards: list[CardR] = []

    def score(self):
        return sum([c.value for c in self._cards])

    def add_card(self, card: CardR):
        self._cards.append(card)





