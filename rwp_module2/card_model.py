from typing import List

from pydantic import BaseModel


class QuizItem(BaseModel):
    question: str
    answer: str


class Quiz(BaseModel):
    items: List[QuizItem]


"""
# Example usage
example_quiz = Quiz(items=[
  {"question": "What does a volt represent?",
   "answer":
    "the electromotive force required to drive an amp of current thru one ohm."},
  # ... add other questions and answers
])
"""
