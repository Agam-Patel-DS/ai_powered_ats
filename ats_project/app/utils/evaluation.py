import os
import groq

# Initialize Groq Client
groq_client = groq.Groq(api_key="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")

def find_strong_weak_points(jd_text, resume_text):
    prompt = f"""
You are an expert AI resume analyzer.

Analyze the following Resume text against the Job Description (JD):

- List strong points (where resume matches JD well) in keywords(two to four words), it should be positive.
- List weak/missing points (where resume does not match JD) in keywords(two to four words). For eg: No Degree, No Experience, it should look negative..

Job Description:
{jd_text}

Resume:
{resume_text}

Respond strictly in this format:

Strong Points:
- Point 1
- Point 2

Weak/Missing Points:
- Point 1
- Point 2
"""

    response = groq_client.chat.completions.create(
        model="llama3-70b-8192",  # Use Groq's model
        messages=[
            {"role": "system", "content": "You are a professional ATS analyzer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=800
    )

    content = response.choices[0].message.content

    # Parse response
    strong_points = []
    weak_points = []

    if "Strong Points:" in content and "Weak/Missing Points:" in content:
        strong_part = content.split("Strong Points:")[1].split("Weak/Missing Points:")[0].strip()
        weak_part = content.split("Weak/Missing Points:")[1].strip()

        strong_points = [point.strip('- ').strip() for point in strong_part.split('\n') if point.strip()]
        weak_points = [point.strip('- ').strip() for point in weak_part.split('\n') if point.strip()]

    return strong_points, weak_points
