import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()
genai.configure(api_key= os.environ.get("GEMINI_API_KEY"))
# The Gemini 1.5 models are versatile and work with both text-only and multimodal prompts
model = genai.GenerativeModel('gemini-1.5-flash-latest')

def get_ai_response(text):
    response = model.generate_content(text + 'if needed, try to answer in brief.')
    response = response.text.split("**")
    response = ' '.join(response)
    return response
