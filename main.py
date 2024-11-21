from flask import Flask, jsonify, request
from chat_gpt.chat_gpt_service import ChatGptService
from chat_gpt.chat_gpt_model import MessageRequestDTO

app = Flask(__name__)

@app.route('/', methods=['GET'])
def generate_tweets():
    # Retrieve query parameters
    context = request.args.get('context')
    question = request.args.get('question', 'Provide 5 tweets on this topic.')

    # Validate input
    if not context:
        return jsonify({'error': 'Context is required'}), 400

    try:
        # Prepare the prompt for ChatGPT
        prompt = f"{context}\n\n{question}"
        request_data = MessageRequestDTO(question=prompt)

        # Call ChatGPT API
        response = ChatGptService.get_ai_model_answer(request_data)

        # Split response into individual tweets
        tweets = response.strip().split('\n')

        # Return formatted response
        return jsonify({
            'result': [tweet.strip() for tweet in tweets if tweet.strip()]
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)