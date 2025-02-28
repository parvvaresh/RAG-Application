def search(query, model, index, ducs, filenames, top_k=3):
    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding, top_k)
    results = [(ducs[idx], filenames[idx])  for idx in indices[0]]
    return results