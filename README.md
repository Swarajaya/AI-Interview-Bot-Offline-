AI Interview Bot (Offline)

An offline AI-powered interview practice application built using Python + Streamlit + Local LLM (TinyLlama).
It simulates real interview scenarios, evaluates answers, and provides feedback — all without internet or paid APIs.

🚀 Features

✅ Auto Interview Mode
✅ Custom Question Mode
✅ Resume-Based Interview
✅ AI Evaluation & Feedback
✅ Runs Fully Offline
✅ Lightweight & Fast
✅ Beginner-friendly UI

🧩 Tech Stack

Python 3.10+

Streamlit – UI framework

Ollama (TinyLlama) – Local LLM

JSON – Session handling

No API Keys Required

📁 Project Structure
AI_Interview_Bot/
│
├── app.py                 # Main application
├── interview_engine.py    # AI logic (question & evaluation)
├── resume_parser.py       # Resume-based interview logic
├── text_to_speech.py      # Optional text-to-speech
├── requirements.txt       # Dependencies
└── README.md              # Project documentation

⚙️ Installation & Setup
1️⃣ Install Dependencies
pip install streamlit ollama

2️⃣ Install Lightweight Model
ollama pull tinyllama

3️⃣ Run the App
streamlit run app.py


Open in browser:

http://localhost:8501

🧠 How It Works
🔹 Auto Interview Mode

System generates a question

User answers

AI evaluates the response

Feedback is shown instantly

🔹 Custom Question Mode

User writes their own interview question

AI evaluates answer quality

🔹 Resume-Based Interview

Paste resume text

AI creates interview questions from it

🧪 Example Output

Question:
What is the difference between functional and object-oriented programming?

Your Answer:
I think both are same.

AI Feedback:

❌ Needs clarity

✔ Explains functional vs object-based approaches

⭐ Score: 4/10

🧠 Suggested improved answer provided