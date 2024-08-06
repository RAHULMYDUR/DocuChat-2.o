import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import faiss

def chunk_documents(documents):
    """Splits documents into manageable chunks."""
    return [doc[i:i + 100] for doc in documents for i in range(0, len(doc), 100)]

def vectorize_chunks(chunks):
    """Vectorizes document chunks using TF-IDF."""
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(chunks).toarray()
    return vectors, vectorizer

def store_vectors_in_faiss(vectors):
    """Stores vectors in FAISS index."""
    d = vectors.shape[1]
    index = faiss.IndexFlatL2(d)
    index.add(np.array(vectors).astype('float32'))
    return index
