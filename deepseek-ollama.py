import pandas as pd
import subprocess
csv_file_path = 'data/fighter_info.csv'
data = pd.read_csv(csv_file_path)
input_text = f"Analyze the following fighter data: {data.head().to_dict()}"
result = subprocess.run(['ollama', 'run', 'deepseek-r1', input_text], capture_output=True, text=True)
print("Model Response:")
print(result.stdout)