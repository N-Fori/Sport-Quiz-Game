# Sport Quiz Game 🧠⚽

This is a graphical True/False quiz game built with Python using the `tkinter` library.  
It fetches live sports-related questions from the Open Trivia Database API.

---

## 📌 Features

- Interactive GUI using `tkinter`
- Dynamic True/False questions from the Open Trivia DB API
- Instant feedback on answers (green/red background)
- Score tracking
- Automatically ends when no more questions remain

---

## 🧩 Technologies Used

- Python 3
- `tkinter` for the graphical user interface
- `requests` to fetch questions from the API
- `html` to clean up text from the API

---

## 🧠 How It Works

1. `question_data` is fetched from the Open Trivia API.
2. Each question is wrapped in a `Question` object.
3. `QuizBrain` manages question flow, scoring, and answer checking.
4. `QuizInterface` handles the visual UI and user interaction with buttons.
5. The game ends once all questions have been answered.

---

## ▶️ Run the Game

Make sure to install the `requests` module if not already installed:

```bash
pip install requests

Then run the main script:

python main.py
Make sure images/true.png and images/false.png exist in an images folder in the same directory.

API Reference
Open Trivia DB: https://opentdb.com/api_config.php

Project Structure
kotlin
Copy
Edit
Sport-Quiz-Game/
├── main.py
├── ui.py
├── quiz_brain.py
├── question_model.py
├── data.py
├── images/
│   ├── true.png
│   └── false.png
└── README.md

Author
Developed by Nandor Forgo
