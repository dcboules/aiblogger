import openai
import os
openai_api_key = os.getenv('OPENAI_API_KEY')

openai.api_key = openai_api_key

