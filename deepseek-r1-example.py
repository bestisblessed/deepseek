# https://dev.to/auden/how-to-call-the-deepseek-r1-api-using-python-an-in-depth-step-by-step-guide-311o
# https://medium.com/@tahirbalarabe2/deepseek-r1-api-interaction-with-python-4fd4217b3b6f

import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('DEEPSEEK_API_KEY')  

url = "https://api.deepseek.com/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

data = {
    "model": "deepseek-chat",  
    # "model": "deepseek-reasoner",
    "messages": [
        {"role": "system", "content": "You are a professional assistant"},
        {"role": "user", "content": "Who are you?"}
    ],
    "stream": False, # Disable streaming ???
    "temperature": 0.7
}
data["stream"] = True # Enable streaming ???
response = requests.post(url, headers=headers, json=data, stream=True)

for line in response.iter_lines():
    if line:
        decoded_line = line.decode("utf-8")
        print(decoded_line)