# first_ai_call.py - Day 3: talk to an AI from Python
# (with model fallback + system instruction)

import os
from dotenv import load_dotenv
from google import genai
from google.genai import errors, types

# 1. Load the secret key from the .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("No API key found! Check your .env file.")
    raise SystemExit

# 2. Create a client: our "phone line" to Gemini
client = genai.Client(api_key=api_key)

# 3. Settings
MODELS = ["gemini-3.8-flash", "gemini-3.5-flash-lite", "gemini-3.6-flash"]

SYSTEM_INSTRUCTION = (
    "You are IOE Saathi, a helpful study assistant for students of the "
    "Institute of Engineering (IOE), Tribhuvan University, Nepal. "
    "Explain things simply, using examples relevant to IOE "
    "Computer and Electronics Engineering courses."
)

question = "Explain the Z-transform to an IOE student in 3 simple sentences."

# 4. Try each model until one answers
for model_name in MODELS:
    try:
        print(f"Trying {model_name}...")
        response = client.models.generate_content(
            model=model_name,
            contents=question,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
            ),
        )
        print(f"\nAnswer from {model_name}:\n")
        print(response.text)
        break  # it worked, so stop trying other models
    except errors.APIError as e:
        print(f"{model_name} failed (error {e.code}). Trying the next one...")
else:
    print("All models are busy right now. Try again in a few minutes.")