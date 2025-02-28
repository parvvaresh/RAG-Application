from DataLoader import LoadDucs
from Embedding import CreateEmbeddings
from Indxer import CreateIndxe
from search import search
from pipeline import GenerateAnswer


def RAG(query = "What is the role of attention mechanism in transformers?"):
    
    # Load PDFs
    pdf_folder = 'ducs'
    documents, filenames = LoadDucs(pdf_folder)

    # Generate Embeddings
    embeddings, model = CreateEmbeddings(documents)

    # Build Index
    index = CreateIndxe(embeddings)

    # Search and Generate Answer
    results = search(query, model, index, documents, filenames)
    answer = GenerateAnswer(query, results)
    return answer["answer"]

#Example Usage
print(RAG())