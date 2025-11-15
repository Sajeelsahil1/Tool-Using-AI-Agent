import os
import google.generativeai as genai
from tools import call_tool


# -----------------------
# GEMINI SETUP
# -----------------------
def configure_gemini():
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY is missing. Add it in the Streamlit sidebar.")

    genai.configure(api_key=api_key)


def get_model():
    configure_gemini()
    return genai.GenerativeModel("models/gemini-2.5-flash")


# -----------------------
# MAIN AGENT LOOP (1 turn)
# -----------------------
def run_agent_once(user_message: str):
    """
    This is called AFTER the user enters the Gemini API key.
    So we create the model HERE instead of at import time.
    """

    model = get_model()   # ✅ NOW SAFE — API key exists

    prompt = f"""
You are a tool-using AI agent.
User said: "{user_message}"

Your job:
1. Detect intent
2. If a tool is needed, return JSON:
   {{
     "tool": "<tool_name>",
     "args": {{ ... }}
   }}
3. If no tool is required, respond normally.
"""

    ai_response = model.generate_content(prompt).text

    # If the model returned tool JSON
    if ai_response.strip().startswith("{") and "\"tool\"" in ai_response:
        import json
        try:
            tool_call = json.loads(ai_response)
            tool_name = tool_call.get("tool")
            args = tool_call.get("args", {})

            result = call_tool(tool_name, args)
            return result

        except Exception as e:
            return {"status": "error", "error": str(e)}

    # No tool needed
    return ai_response
