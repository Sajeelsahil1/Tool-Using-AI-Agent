import os
import smtplib
import traceback
from email.mime.text import MIMEText
import requests
import json

BASE_DIR = os.path.join(os.path.dirname(__file__), "agent_files")
os.makedirs(BASE_DIR, exist_ok=True)


# ---------------------------------------------------
# 🔧 1) Write File
# ---------------------------------------------------
def write_file(file_path: str, content: str):
    try:
        full_path = os.path.join(BASE_DIR, file_path)

        # Ensure directory exists
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

        return {"status": "written", "path": full_path}

    except Exception as e:
        traceback.print_exc()
        return {"status": "error", "error": str(e)}


# ---------------------------------------------------
# 🔧 2) Read File
# ---------------------------------------------------
def read_file(file_path: str):
    try:
        full_path = os.path.join(BASE_DIR, file_path)

        if not os.path.exists(full_path):
            return {"status": "error", "error": "File not found"}

        with open(full_path, "r", encoding="utf-8") as f:
            return {"status": "ok", "content": f.read()}

    except Exception as e:
        traceback.print_exc()
        return {"status": "error", "error": str(e)}


# ---------------------------------------------------
# 🔧 3) Simple Web Search (DuckDuckGo)
# ---------------------------------------------------
def search_web(query: str):
    try:
        url = "https://api.duckduckgo.com/"
        params = {"q": query, "format": "json"}

        response = requests.get(url, params=params)
        data = response.json()

        return {
            "status": "ok",
            "query": query,
            "abstract": data.get("Abstract", ""),
            "related": data.get("RelatedTopics", [])
        }

    except Exception as e:
        traceback.print_exc()
        return {"status": "error", "error": str(e)}


# ---------------------------------------------------
# 🔧 4) SEND EMAIL — Gmail SMTP With App Password
# ---------------------------------------------------
def send_email(to: str, subject: str, body: str):
    gmail_user = os.environ.get("GMAIL_USER")
    gmail_pass = os.environ.get("GMAIL_APP_PASSWORD")

    if not gmail_user or not gmail_pass:
        return {
            "status": "error",
            "error": "SMTP credentials missing (GMAIL_USER / GMAIL_APP_PASSWORD)"
        }

    try:
        msg = MIMEText(body)
        msg["From"] = gmail_user
        msg["To"] = to
        msg["Subject"] = subject

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(gmail_user, gmail_pass)
        server.sendmail(gmail_user, [to], msg.as_string())
        server.quit()

        return {
            "status": "sent",
            "to": to,
            "subject": subject
        }

    except Exception as e:
        print("\n🔥 SMTP ERROR CAUGHT IN send_email TOOL")
        print("Error message:", str(e))
        traceback.print_exc()
        return {"status": "error", "error": str(e)}


# ---------------------------------------------------
# 🔧 TOOL DISPATCHER
# ---------------------------------------------------
def call_tool(tool_name: str, args: dict):
    try:

        if tool_name == "write_file":
            return write_file(args["path"], args["content"])

        if tool_name == "read_file":
            return read_file(args["path"])

        if tool_name == "search_web":
            return search_web(args["query"])

        if tool_name == "send_email":
            return send_email(args["to"], args["subject"], args["body"])

        return {"status": "error", "error": f"Unknown tool: {tool_name}"}

    except Exception as e:
        print("\n❌ TOOL ROUTER CRASH:", tool_name)
        traceback.print_exc()
        return {"status": "error", "error": str(e)}
