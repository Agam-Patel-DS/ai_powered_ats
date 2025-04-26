from sentence_transformers import SentenceTransformer
from app.config import EMBEDDING_MODEL_NAME

model = SentenceTransformer(EMBEDDING_MODEL_NAME)

def get_embedding(text):
    return model.encode(text)
