# API for Contextual Responses Using ChatGPT

---

## Project Description
This project provides a lightweight Flask-based API that accepts a `context` and a `question` as query parameters and returns a JSON response with relevant posts or messages. The API leverages OpenAI's ChatGPT to dynamically generate context-aware responses, providing customizable outputs. The application can be accessed via a public IP and is designed for scalability and integration into various systems.

---

## Setup Instructions

### 1. Prerequisites
- Python 3.6+ installed on your server
- OpenAI API Key (required for ChatGPT integration)
- A server environment (e.g., Ubuntu on a DigitalOcean Droplet)
### 2. Clone the Repository
```bash
git clone [https://github.com/your-repo-name/api-chatgpt-integration.git](https://github.com/Oliz888/api-test)
cd api-test
```
### 3. Create and Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```
### 4. Install Required Dependencies
```bash
pip install -r requirements.txt
```
### 5. Configure OpenAI API Key
```bash
nano .env
OPENAI_API_KEY=your_openai_api_key
```
### 6. Run the Flask Application Locally
```bash
python main.py
```
### 7. Test Locally
```bash
http://127.0.0.1:3000/?context=I%20support%20assembly%20rights&question=Give%20me%205%20posts
```
### 8. Deploy with Gunicorn
```bash
gunicorn --bind 0.0.0.0:3000 app:app
```
9. Configure Nginx as a Reverse Proxy
Ensure Nginx routes requests to the Flask application (details covered in the setup guide).

## API Usage
```vbnet
http://<your-public-ip>:3000/
```
Query Parameters
context (string): The main topic or idea for the response.
question (string): The specific request or query for information.
```perl
http://206.81.8.202:3000/?context=I%20support%20assembly%20rights&question=Give%20me%205%20posts
```
## Test Cases
1. Valid Input - Typical Case
   ```
   http://206.81.8.202:3000/?context=I%20support%20assembly%20rights&question=Give%20me%205%20posts
   http://206.81.8.202:3000/?context=Freedom%20of%20speech&question=Give%20me%205%20examples
   http://206.81.8.202:3000/?context=Education%20reform&question=Give%20me%2010%20posts
   http://206.81.8.202:3000/?context=Education%20reform&question=Give%20me%2010%20tweets
```
