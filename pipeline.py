from transformers import pipeline  # type: ignore


def GenerateAnswer(query, results):
    qa_pipeline = pipeline("question-answering")
    context = " ".join([result for result, _ in results])
    answer = qa_pipeline(question=query, context=context)
    return answer