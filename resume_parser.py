import ollama

def generate_questions_from_resume(text):
    prompt = f"""
Given this resume content:

{text}

Generate 3 interview questions based on skills and experience.
"""
    res = ollama.chat(
        model="tinyllama",
        messages=[{"role": "user", "content": prompt}]
    )
    return res["message"]["content"]
