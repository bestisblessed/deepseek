import pandas as pd
import subprocess

csv_file_1 = 'data/fighter_info.csv'
csv_file_2 = 'data/event_data_sherdog.csv'
df1 = pd.read_csv(csv_file_1)
df2 = pd.read_csv(csv_file_2)
input_text = (
    f"Analyze the following CSV files: {df1} and {df2}. "
    "List me all column names and general statistics for each dataset and how many missing values are in each column. "
    # "Extract key trends, patterns, averages, outliers, and insights from each dataset. "
    # "Once your analysis is complete, use these datasets and insights to answer any questions I ask. "
    # "Please reason step by step and provide your final answer within \\boxed{...}."
)
# input_text = f"Analyze the following CSV files: {csv_file_1}, {csv_file_2}"
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