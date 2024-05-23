from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()
client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
)


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

# print(completion.choices[0].message)

# print(os.environ.get("OPENAI_API_KEY"))
# print(os.environ['OPENAI_API_KEY'])
# print(os.environ)
print(os.getenv("OPENAI_API_KEY"))