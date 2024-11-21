import os
from openai import OpenAI
from chat_gpt.chat_gpt_model import MessageRequestDTO

from dotenv import load_dotenv
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ChatGptService:
    @classmethod
    def get_ai_model_answer(cls, data: MessageRequestDTO):
        try:
            # Debug: Log the request payload
            print("Requesting ChatCompletion with:", data)

            # Call the OpenAI API using the client
            response = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": data.question},
                ],
                model=data.model_id,
                temperature=data.temperature,
                max_tokens=data.max_tokens,
            )

            # Debug: Log the raw API response
            print("Raw Response from OpenAI API:", response)

            # Extract the assistant's response from the choices
            result = response.choices[0].message.content
            print("Extracted Result:", result)

            return result
        except Exception as e:
            # Log and raise the error
            print("Error during OpenAI API call:", str(e))
            raise Exception(f"OpenAI API error: {str(e)}")

    @classmethod
    def list_models(cls):
        try:
            # List all available models
            response = client.models.list()
            print("Available models:", response)
            return response
        except Exception as e:
            # Log and raise the error
            print("Error during OpenAI model listing:", str(e))
            raise Exception(f"Error listing models: {str(e)}")
