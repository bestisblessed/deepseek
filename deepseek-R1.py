import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv('DEEPSEEK_API_KEY')
client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
csv_file_path = 'data/fighter_info.csv'
data = pd.read_csv(csv_file_path)
example_question = f"Analyze the following fighter data: {data.head().to_dict()}"
messages = [
    {"role": "system", "content": "You are an analytical assistant."},
    {"role": "user", "content": example_question}
]
response = client.chat.completions.create(
    model="deepseek-reasoner",
    # model="deepseek-chat",
    messages=messages
)
print("Model Response:")
print(response.choices[0].message.content)