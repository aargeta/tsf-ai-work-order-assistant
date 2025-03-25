import os
import openai
from pathlib import Path

# Load OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Path to your prompt templates
PROMPT_DIR = Path(__file__).resolve().parent.parent / "prompts"

def load_prompt(filename):
    path = PROMPT_DIR / filename
    with open(path, "r") as file:
        return file.read()

def extract_work_order_data(email_body):
    prompt = load_prompt("extract_prompt.txt")
    full_prompt = prompt.replace("{{email_body}}", email_body.strip())

    print("🔍 Calling OpenAI to extract fields...")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that extracts structured data from emails."},
            {"role": "user", "content": full_prompt}
        ],
        temperature=0.2
    )
    return response["choices"][0]["message"]["content"]

def generate_response_email(extracted_json):
    prompt = load_prompt("reply_prompt.txt")
    full_prompt = prompt.replace("{{extracted_json}}", extracted_json.strip())

    print("✉️ Generating client response...")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a professional project coordinator replying to client requests."},
            {"role": "user", "content": full_prompt}
        ],
        temperature=0.5
    )
    return response["choices"][0]["message"]["content"]

