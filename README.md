🚀 Tool-Using AI Agent (Gemini + Streamlit)

An intelligent AI agent powered by Google Gemini that can execute real tools, including:

✅ Creating files
✅ Reading files
✅ Writing files
✅ Sending emails
✅ Executing shell commands
✅ Maintaining conversation history
✅ Logging tool execution

Built with Python + Streamlit, this project demonstrates real-world AI agent capabilities with secure API key handling.

📦 Features
🔧 AI Tools

File Management

Create new files

Read existing files

Write/overwrite files

Email Sending

Uses Gmail SMTP

Requires Gmail App Password

Command Execution

Run Windows/macOS/Linux shell commands

Capture output + errors

Conversation Memory

Each agent run returns tool actions

Debug Logging

Every tool run prints logs to terminal

Helps track errors instantly

📁 Project Structure
📦 Tool-Using-AI-Agent
 ┣ 📜 app.py            # Streamlit UI
 ┣ 📜 agent.py          # Gemini model logic
 ┣ 📜 tools.py          # All executable tools
 ┣ 📁 agent_files       # Files created by AI agent
 ┗ 📜 README.md

🔑 Setup Instructions
1️⃣ Install required packages
pip install -r requirements.txt

2️⃣ Set your environment variables in the Streamlit sidebar

Gemini API Key

(Optional) Gmail Email

(Optional) Gmail App Password

⚠️ Important: Normal Gmail password will NOT work.
You must create a Gmail App Password:

🔒 How to Generate Gmail App Password

Go to
https://myaccount.google.com/apppasswords

Select Mail

Select Windows Computer

Click Generate

Copy the 16-character password

Paste it in the Streamlit sidebar

▶️ Run the App
streamlit run app.py

🧪 Example Commands for the Agent
Create a file
Create a file called notes.txt containing "Hello world!"

Read a file
Read the file notes.txt

Send an email
Send email to example@gmail.com saying hello

Run a command
Run the command "dir"

📝 Logging

All tools print logs like:

[LOG] Running tool: create_file
[LOG] File created at: agent_files/test.txt


If an error happens, you’ll see:

[ERROR] SMTP credentials missing

🧑‍💻 Author

Sajeel Sahil

GitHub Repo:
https://github.com/Sajeelsahil1/Tool-Using-AI-Agent
