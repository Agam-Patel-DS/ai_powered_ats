from app.utils.text_extraction import extract_text
from app.utils.text_cleaning import clean_text
from app.utils.embedding_model import get_embedding
from app.utils.similarity_scoring import calculate_similarity_ai
from app.utils.evaluation import find_strong_weak_points
from app.utils.report_generator import create_excel_report
from app.config import THRESHOLD_SCORE

def process_company(jd_file, resumes):
    jd_text = clean_text(extract_text(jd_file))
    jd_embedding = get_embedding(jd_text)

    results = []
    for resume_file in resumes:
        resume_text = clean_text(extract_text(resume_file))
        resume_embedding = get_embedding(resume_text)

        score = calculate_similarity_ai(jd_embedding, resume_embedding)
        strong, weak = find_strong_weak_points(jd_text, resume_text)

        status = 'Accepted' if score >= THRESHOLD_SCORE else 'Rejected'

        results.append({
            'Resume Name': resume_file.name,
            'Score': round(score, 2),
            'Strong Points': ', '.join(strong),
            'Weak Points': ', '.join(weak),
            'Status': status
        })

    create_excel_report(results)
    return results
