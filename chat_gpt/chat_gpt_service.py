import openai
import os
from chat_gpt.chat_gpt_model import MessageRequestDTO
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

class ChatGptService:

    @classmethod
    def get_ai_model_answer(cls, data: MessageRequestDTO):
        # Construct the prompt using both context and the question
        prompt = f"{data.context}\n\n{data.question}"

        # Call OpenAI to get a response, using the new ChatCompletion API
        response = openai.ChatCompletion.create(
            model=data.model_id,
            messages=[
                {"role": "system", "content": "You are an AI that helps generate social media posts."},
                {"role": "user", "content": prompt}
            ],
            temperature=data.temperature,
            max_tokens=data.max_tokens,
            n=5  # Ask for 5 separate responses (for 5 tweets)
        )

        # Extract the list of tweets from the response
        tweets = [choice['message']['content'] for choice in response['choices']]

        # Return the list of tweets as a joined string or as a list, depending on your needs
        return tweets

    @classmethod
    def list_models(cls):
        return openai.Model.list()
