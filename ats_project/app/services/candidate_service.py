from app.utils.text_extraction import extract_text
from app.utils.text_cleaning import clean_text
from app.utils.embedding_model import get_embedding
from app.utils.similarity_scoring import calculate_similarity_ai
from app.utils.evaluation import find_strong_weak_points
from app.config import THRESHOLD_SCORE

def process_candidate(jd_file, resume_file):
    jd_text = clean_text(extract_text(jd_file))
    resume_text = clean_text(extract_text(resume_file))

    jd_embedding = get_embedding(jd_text)
    resume_embedding = get_embedding(resume_text)

    score = calculate_similarity_ai(jd_embedding, resume_embedding)
    strong, weak = find_strong_weak_points(jd_text, resume_text)

    status = 'Accepted' if score >= THRESHOLD_SCORE else 'Rejected'

    suggestions = []
    if score < THRESHOLD_SCORE:
        suggestions.append("Consider adding missing skills/keywords related to the job.")

    return {
        'Score': round(score, 2),
        'Strong Points': strong,
        'Weak Points': weak,
        'Suggestions': suggestions,
        'Status': status
    }
