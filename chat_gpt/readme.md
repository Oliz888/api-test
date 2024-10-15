# ChatGPT Flask API Service

This project is a Flask-based API that interacts with OpenAI's GPT models to generate responses, such as social media posts or tweets, based on user input. It uses an `.env` file to securely load API keys and other configuration details.

## Features
- Accepts user inputs with context and questions to generate AI-generated social media posts.
- Returns multiple responses (e.g., five tweets) using OpenAI's ChatCompletion API.
- Lists available models from the OpenAI API.
- Environment variables are securely loaded from a `.env` file.

## Requirements

- Python 3.x
- OpenAI Python Client Library (`openai`)
- Flask
- Python-dotenv

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2. **Create and activate a virtual environment (optional but recommended):**
     ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Set up your .env file**
   - Create a .env file in the root directory of the project and add your OpenAI API key:
   ```bash
   OPENAI_API_KEY=your_openai_api_key_here

4. **Run the Flask server:**
    ```bash
   python app.py
   ```
   The server will be available at http://127.0.0.1:3001/.

## Endpoints

1. **`/message` (POST)**
This endpoint accepts a JSON body with a context and a question and returns multiple AI-generated responses (e.g., 5 tweets).

Example Request:
```json
{
  "context": "I support abortion because it is a fundamental human right.",
  "question": "Give me 5 tweets on this topic."
}
   ```
```json
{
  "result": [
    "Everyone deserves the right to choose what's best for their own body. #ProChoice #ReproductiveRights",
    "Abortion is healthcare. No one should be forced into parenthood against their will. #MyBodyMyChoice",
    "Protecting the right to choose means protecting the freedom to live life on your own terms. #AbortionRights",
    "It's about bodily autonomy. Women should always have the power to decide their own future. #ProChoice",
    "Abortion isn't just about choice—it's about dignity and equality. We must stand for reproductive rights. #HumanRights"
  ]
}
   ```
## Project Structure
```bash
├── app.py                 # Entry point to start the Flask app
├── chat_gpt               # Directory containing all logic related to ChatGPT service
│   ├── __init__.py        # Package initializer
│   ├── chat_gpt_service.py# Main service interacting with OpenAI API
│   ├── chat_gpt_controller.py # Flask routes for handling API requests
│   ├── chat_gpt_model.py  # Data model for handling user requests
├── .env                   # Environment variables (should be in .gitignore)
├── requirements.txt       # Dependencies needed for the project
└── README.md              # This file
  ```
## Environment Variables
OPENAI_API_KEY: Your OpenAI API key (must be set in the .env file).

## How to Use
Send a POST request to the /message endpoint with a context and a question.

## License
This project is licensed under the MIT License - see the LICENSE file for details.