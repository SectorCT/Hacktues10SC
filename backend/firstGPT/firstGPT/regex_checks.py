import re
"""
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("api_key")
le_format = os.getenv("le_format")

client = OpenAI(api_key=api_key)

test = "Дадена е правилна четириъгълна призма ACBDA1B1C1D1 с основен ръб Ab = 3 и околен ръб AA1 = 4. Намерете косинуса на ъгъл между AD1 и BC."

prompt = [
    {"role": "system", "content": "You are a mathematical assistant and you are going to work on stereometry qustions."},
    {"role": "user", "content": test},
    {"role": "user", "content": \
     "Дай ми координатите на върховете на фигурата в JSON формат (Форматът за JSON файла е: {le_format}) и кои двойки точки се свързват в отсечки. Отговори само с JSON файла без нищо друго. На английски език."},
]

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=prompt,
  max_tokens = 300
  #stream=True
)
"""
def r_check(api_response):
    pattern = r'\{\s*"vertices": \{(\s*".*": \[.+, .+, .+\],*\s*)+\},\s*"edges": \[(\s*\[".*", ".*"\]\s*,*)+\]\s*\}'

    if re.match(pattern, api_response):
        print("Pattern matched.")
        return 0
    else:
        print("Pattern not matched.")
        return -1
