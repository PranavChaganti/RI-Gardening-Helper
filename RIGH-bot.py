import html, re
from flask import Flask, render_template, request, jsonify, Response
import getpass
import os
import openai
#os.environ['OPENAI_API_KEY'] = getpass.getpass("OpenAI API Key: ")
openai.api_key = os.getenv('MY-OPENAI-KEY')
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
import nest_asyncio

nest_asyncio.apply()

import getpass
import os

#os.environ["LLAMA_CLOUD_API_KEY"] = getpass.getpass()
LLAMA_CLOUD_API_KEY = os.getenv('LLAMA_CLOUD_API_KEY')
#LLAMA_CLOUD_API_KEY='llx-FATx2gexPefGWiVotb8SHCIzHOy6QAIh0LZSSVP3IvZ8171K'
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_parse import LlamaParse

#documents = SimpleDirectoryReader("/Users/pc/aiml/ai-env/Data").load_data()
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
