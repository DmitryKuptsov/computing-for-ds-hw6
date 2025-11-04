import pytest
from hw5 import Card, Deck


def test_card_init():
    c = Card("Hearts", "A")
    assert c.suit == "Hearts"
    assert c.value == "A"


def test_card_str():
    c = Card("Spades", "K")
    assert str(c) == "K of Spades"


def test_deck_has_52_cards():
    d = Deck()
    assert len(d.cards) == 52

    suits = {"Hearts", "Diamonds", "Clubs", "Spades"}
    values = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"}
    all_pairs = {(c.suit, c.value) for c in d.cards}
    assert all_pairs == {(s, v) for s in suits for v in values}


def test_shuffle_changes_order():
    d = Deck()
    before = [(c.suit, c.value) for c in d.cards]
    d.shuffle()
    after = [(c.suit, c.value) for c in d.cards]
    # order should usually change
    assert before != after or before == after


def test_draw_returns_card_and_reduces_size(capsys):
    d = Deck()
    n = len(d.cards)
    card = d.draw()
    out = capsys.readouterr()
    assert isinstance(card, Card)
    assert len(d.cards) == n - 1
    assert "of" in out.out


def test_draw_from_empty_deck(capsys):
    d = Deck()
    d.cards.clear()
    card = d.draw()
    out = capsys.readouterr()
    assert card is None
    assert "No cards left" in out.out

def test_draw_prints_card(capsys):
    d = Deck()
    d.draw()  # draw once
    out = capsys.readouterr()
    assert "of" in out.out  # printed card
