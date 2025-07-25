# 🎯 Quizzy

**Quizzy** is a responsive and dark-mode-friendly trivia quiz application built with Flask. It pulls real-time questions from the [Open Trivia DB API](https://opentdb.com/), tracks your score, and supports difficulty and category selection. Includes a leaderboard to compete with friends!

---

## ✨ Features

- 🔢 10 multiple-choice questions per quiz
- 🎨 Responsive design with Dark Mode toggle
- 🎯 Difficulty and category selection
- 📊 Progress bar and real-time score tracking
- 🧠 Dynamic questions via Open Trivia API
- 🏆 Leaderboard with name entry
- 📱 Mobile-optimized interface

---

## 🚀 Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/quizzy.git
    cd quizzy
2. Install dependencies
    ```bash
    pip install -r requirements.txt  
3. Run the app
    ```bash
    python app.py
Visit http://localhost:5000 in your browser.

---

## 🌐 Mobile Testing
To test on your phone (while on the same Wi-Fi)
```bash
# In app.py
    if __name__ == '__main__':
         app.run(debug=True, host='0.0.0.0', port=5000)
```
Then visit http://<your-ip>:5000 from your mobile browser.

---

## 🛠 Tech Stack
Backend: Python, Flask

Frontend: HTML5, CSS3, JavaScript

API: Open Trivia DB

---

## 📂 Project Structure
```bash
quizzy/
│
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   ├── question.html
│   ├── result.html
│   └── leaderboard.html
├── static/
│   ├── style.css
│   └── script.js
```

---

## 🤝 Contributing
Pull requests are welcome! Feel free to fork the repo and submit improvements.

---

## 📄 License
MIT License. See LICENSE for more information.

---

## 🧑‍💻 Author
Abdulwahab Uthman
For questions or collaboration: Abduluthman278@gmail.com
