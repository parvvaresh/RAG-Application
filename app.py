from flask import Flask, render_template, request, jsonify
from rag import RAG

app = Flask(__name__)


@app.route("/")
def index_page():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    query = data.get("query", "")
    if not query:
        return jsonify({"error": "Empty query provided"}), 400
    answer = RAG(query)
    return jsonify({"answer": answer})



if __name__ == "__main__":
    app.run(debug=True)