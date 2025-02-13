#!/bin/bash
# run_ollama_gui.sh

# Create a new tmux session named "deepseek"
tmux new-session -d -s deepseek

# In the first pane, run the Ollama server
tmux send-keys -t deepseek "echo 'Starting Ollama server...'" C-m
tmux send-keys -t deepseek "ollama serve" C-m

# Split the window horizontally (change -h to -v for vertical split if preferred)
tmux split-window -h -t deepseek

sleep 3 

# In the new pane, check for an existing open-webui container and start it if found;
# otherwise, run a new container using the local image.
tmux send-keys -t deepseek:0.1 "echo 'Checking for existing open-webui container...'" C-m
tmux send-keys -t deepseek:0.1 "if [ \$(docker ps -a -q -f name=open-webui) ]; then echo 'Container exists. Starting it...'; docker start open-webui; else echo 'Container not found. Creating a new one...'; docker run -d --name open-webui -p 3000:3000 -e PORT=3000 -v open-webui-data:/app/data ghcr.io/open-webui/open-webui:main; fi" C-m

# Optional: Return to the first pane
tmux select-pane -t deepseek:0.0

# Attach to the tmux session so you can see the split view
tmux attach-session -t deepseek

# When the tmux session is terminated (i.e. you exit), perform cleanup.
echo "tmux session ended. Cleaning up Docker container..."
docker rm -f open-webui
