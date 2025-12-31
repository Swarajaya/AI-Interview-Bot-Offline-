import ollama

def evaluate_answer(question, answer):
    prompt = f"""
You are a professional technical interviewer.

Question:
{question}

Candidate Answer:
{answer}

Give:
1. Score out of 10
2. Strengths
3. Weaknesses
4. Improved sample answer
"""

    response = ollama.chat(
        model="tinyllama",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]


def generate_question(topic="general"):
    prompt = f"Ask one technical interview question on {topic}."
    response = ollama.chat(
        model="tinyllama",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]
