import openai
import os
openai_api_key = os.getenv('OPENAI_API_KEY')

openai.api_key = openai_api_key

def generate_blog(paragraph_topic):
    response = openai.completions.create(
        model = 'gpt-3.5-turbo-instruct',
        prompt = 'Write a paragraph about the following topic. ' + paragraph_topic,
        max_tokens = 400,
        temperature = 0.3
    )
    retrieve_blog = response.choices[0].text
    return retrieve_blog
print(generate_blog('Why NYC is better than your city.'))

