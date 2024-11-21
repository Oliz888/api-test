from flask import Blueprint, request, jsonify
from chat_gpt.chat_gpt_service import ChatGptService
from chat_gpt.chat_gpt_model import MessageRequestDTO

chat_gpt_route_path = 'chat-gpt-ai'

chat_gpt_route = Blueprint(chat_gpt_route_path, __name__)

@chat_gpt_route.route('/message', methods=['POST'])
def get_ai_model_answer():
    try:
        # Debug: Print the request body
        print("Received request body:", request.json)

        # Parse the request data
        body = request.json
        request_data = MessageRequestDTO.new_instance_from_flask_body(body)

        # Call the service to get the answer
        answer = ChatGptService.get_ai_model_answer(request_data)

        # Return the response
        return jsonify({'result': answer})
    except Exception as e:
        # Debug: Print the error
        print("Error in /message route:", str(e))
        return jsonify({'error': str(e)}), 500
