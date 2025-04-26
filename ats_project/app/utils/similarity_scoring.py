from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(embedding1, embedding2):
    return cosine_similarity([embedding1], [embedding2])[0][0] * 100

import re

from groq import Groq

# Initialize Groq Client (setup only once)
groq_client = Groq(api_key="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")

def calculate_similarity_ai(jd_text, resume_text):
    """
    Uses Groq LLaMA3 to score similarity between JD and Resume
    """

    prompt = f"""
You are an expert resume evaluator.

Given the following Job Description (JD) and Resume text, give a matching score between 0 and 100.

Scoring Rules:
- 90-100: Almost perfect match.
- 70-89: Good match but needs slight improvement.
- 50-69: Average match, several important points missing.
- Below 50: Poor match.

Only give the numeric score. No explanation.
return ONLY integer

Job Description:
{jd_text}

Resume:
{resume_text}
"""

    response = groq_client.chat.completions.create(
        model="llama3-8b-8192",  # 🦙 Groq's fast LLaMA3 model
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.0,  # No randomness; consistent scoring
        max_tokens=10,    # We expect just a number
    )

    score_text = response.choices[0].message.content.strip()

    match = re.search(r"\d+", score_text)
    if match:
        score = float(match.group())
        return min(max(score, 0), 100)  # Clamp between 0-100
    else:
        return 0.0