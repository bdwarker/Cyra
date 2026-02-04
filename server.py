import os
from dotenv import load_dotenv
load_dotenv()

OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY")
if not OLLAMA_API_KEY:
    raise ValueError("OLLAMA_API_KEY not found in environment variables.")
print("OLLAMA_API_KEY loaded successfully.")
from ollama import chat, ChatResponse

response: ChatResponse = chat(model='granite4', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)