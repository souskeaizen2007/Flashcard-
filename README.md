# 🃏 French Flash Card App

A beginner-friendly Python project built using **Tkinter** and **Pandas** that helps users learn basic French vocabulary interactively using flashcards.

## 📸 Screenshots

![Flashcard Front](card_front.png)  
![Flashcard Back](card_back.png)

## 🚀 Features

- Displays French words on a flashcard.
- Automatically flips the card after 3 seconds to reveal the English translation.
- Two buttons to mark the word as known or unknown.
- Words marked as known are removed from the learning list and saved persistently.
- Smooth and clean GUI built with Tkinter.

## 📁 Files Required

Make sure the following files are in the same directory:
- `french_words.csv` – The original dataset of French-English word pairs.
- `words_to_learn.csv` – Automatically created after marking known words.
- `card_front.png` – Flashcard front image.
- `card_back.png` – Flashcard back image.
- `right.png` – Tick button image (✔️).
- `wrong.png` – Cross button image (❌).

## 📦 Dependencies

- Python 3.x
- pandas
- tkinter (comes with Python)

Install pandas if not already installed:

```bash
pip install pandas
