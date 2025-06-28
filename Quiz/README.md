# 🧠 Quiz Game Project

A simple console-based quiz game built using Python. This interactive game asks the user True/False questions and keeps track of their score.

---

## 📌 Overview

This project simulates a basic quiz game where users are presented with a series of multiple-choice (True/False) questions. The game keeps track of the user's score and displays feedback after each question.

It demonstrates object-oriented programming concepts in Python by using classes to model questions, manage the quiz logic, and handle user input/output.

---

## 🔍 Features

- Interactive command-line interface
- Score tracking
- Instant feedback after each question
- Modular code structure using classes:
  - `Question`: Models a single quiz question
  - `QuizBrain`: Manages the quiz flow and scoring
  - `data.py`: Contains the list of quiz questions and answers

---

## 📁 File Structure

| File            | Description |
|-----------------|-------------|
| `main.py`       | Entry point of the application. Runs the quiz loop. |
| `quiz_brain.py` | Contains the `QuizBrain` class that manages quiz logic. |
| `question_model.py` | Defines the `Question` class to store question-answer pairs. |
| `data.py`       | Stores the quiz questions and answers in a list of dictionaries. |

---

## ▶️ How to Run

1. Make sure you have Python installed (`3.x` recommended).
2. Open your terminal or command prompt.
3. Navigate to the directory containing the files:

   ```bash
   cd path/to/quiz-game-start
4. Run the file
   ```
   python main.py
