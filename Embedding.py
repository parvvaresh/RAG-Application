from sentence_transformers import SentenceTransformer

def CreateEmbeddings(ducs: list) -> list:
    # Load a pre-trained embedding model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Generate embeddings for each document
    embeddings = model.encode(ducs, show_progress_bar=True)
    return embeddings, model