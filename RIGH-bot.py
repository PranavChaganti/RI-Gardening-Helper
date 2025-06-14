import html, re
from flask import Flask, render_template, request, jsonify, Response
import getpass
import os
import openai
openai.api_key = os.getenv('MY_OPENAI_KEY')
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
import nest_asyncio

nest_asyncio.apply()

LLAMA_CLOUD_API_KEY = os.getenv('LLAMA_CLOUD_API_KEY')
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_parse import LlamaParse

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
app = Flask(__name__)

# Example chatbot function
def chatbot_response(message):
    response = query_engine.query(message)
    return f"{response}"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.form["message"]
    bot_reply = chatbot_response(user_message)
    formatted_response = bot_reply.replace("\n", "<br>")
    url_pattern = r'(https?://[^\s]+)'
    formatted_response = re.sub(url_pattern, r'<a href="\1" target="_blank">\1</a>', formatted_response)
    return jsonify({"response": formatted_response})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # 👈 THIS is the key line
    app.run(host='0.0.0.0', port=port)
