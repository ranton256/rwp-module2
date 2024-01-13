import pytest

from rwp_module2.card_model import QuizItem
from rwp_module2.cli_cards import load_flashcards


# Test for load_flashcards function
def test_load_flashcards():
    quiz = load_flashcards("tests/test_data/test_flashcards.json")
    assert len(quiz.items) > 0
    assert isinstance(quiz.items[0], QuizItem)
