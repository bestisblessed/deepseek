import pandas as pd
import subprocess

data = pd.read_csv('data/fighter_info.csv')
input_text = f"Analyze the following fighter data: {data.head().to_dict()}"
print("Running the model, please wait...")

# Run the model using Ollama
process = subprocess.Popen(
    ['ollama', 'run', 'deepseek-r1', input_text],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# Stream the output line by line
for line in process.stdout:
    print(line, end='')  # Print each line as it comes in

# Wait for the process to complete
process.wait()

# Check for any errors
if process.returncode != 0:
    error_message = process.stderr.read()
    print(f"Error: {error_message}")

# Stop the model after processing
subprocess.run(['ollama', 'stop', 'deepseek-r1'])
print("Model has been stopped.")