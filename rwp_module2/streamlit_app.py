import os
import sys

import streamlit as st

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
print(f"SRC_DIR is {SRC_DIR}")

APP_DIR = os.path.dirname(SRC_DIR)
print(f"APP_DIR is {APP_DIR}")

sys.path.append(APP_DIR)

from rwp_module2.card_model import Quiz  # noqa: E402
from rwp_module2.cli_cards import load_flashcards  # noqa: E402

# Streamlit app
st.title("Flashcard Quiz App")


sample_data = {
    "items": [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is 2+2?", "answer": "4"}
        # Add more questions and answers here
    ]
}

quizzes = {
    "Sample": Quiz.model_validate(sample_data),
    "Electricity 1": load_flashcards("data/electricity1.json"),
    "Electricity 2": load_flashcards("data/electricity2.json"),
}


def select_quiz():
    st.session_state["q_idx"] = 0
    st.session_state["q_shown"] = False


q_key = st.selectbox("Choose a question set", quizzes.keys(), on_change=select_quiz)

if q_key:
    quiz = quizzes[q_key]


if "q_idx" not in st.session_state:
    st.session_state["q_idx"] = 0

if "q_shown" not in st.session_state:
    st.session_state["q_shown"] = False

q_idx = st.session_state["q_idx"]
q_shown = st.session_state["q_shown"]

if quiz:
    n_items = len(quiz.items)

    if st.button("Previous Question", disabled=q_idx < 1):
        # print(f"you clicked previous, q_idx={q_idx}")
        q_idx -= 1
        q_shown = False
        st.session_state["q_idx"] = q_idx
        st.session_state["q_shown"] = q_shown
        st.rerun()

    if st.button("Next Question", disabled=q_idx >= n_items - 1):
        # print(f"you clicked next, q_idx={q_idx}")
        q_idx += 1
        q_shown = False
        st.session_state["q_idx"] = q_idx
        st.session_state["q_shown"] = q_shown
        st.rerun()

    i = q_idx
    item = quiz.items[i]

    def btn_clicked(btn):
        # print(f"You clicked {btn}")
        q_shown = btn == "show"
        st.session_state["q_shown"] = q_shown

    with st.container():
        st.markdown(f"### Question {i+1} of {n_items}")
        st.text(item.question)
        if not q_shown:
            if st.button(
                f"Show Answer for Question {i}", on_click=btn_clicked, args=("show",)
            ):
                st.write("you clicked show")
        else:
            if st.button(
                f"Hide Answer for Question {i}", on_click=btn_clicked, args=("hide",)
            ):
                st.write("you clicked hide")

        st.session_state["q_shown"] = q_shown
        if q_shown:
            st.markdown(item.answer)
