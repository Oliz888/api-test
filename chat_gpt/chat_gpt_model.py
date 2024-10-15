from dataclasses import dataclass, field
from typing import Optional

DEFAULT_MODEL = 'gpt-4o-mini'
DEFAULT_TEMPERATURE = 0.9
DEFAULT_MAX_TOKENS = 1024


@dataclass
class MessageRequestDTO:
    question: str  # This will be your request, like "Give me 5 tweets"
    context: Optional[str] = None  # This is the context like "I support abortion because xxx"
    max_tokens: Optional[int] = field(default=DEFAULT_MAX_TOKENS)
    temperature: Optional[float] = field(default=DEFAULT_TEMPERATURE)
    model_id: Optional[str] = field(default=DEFAULT_MODEL)

    @staticmethod
    def new_instance_from_flask_body(data: dict) -> 'MessageRequestDTO':
        if 'question' not in data:
            raise Exception('question attribute not found')

        res = MessageRequestDTO(
            question=data['question'],
            context=data.get('context')  # Extract context if provided
        )

        for attr in ['max_tokens', 'temperature', 'model_id']:
            if attr in data:
                setattr(res, attr, data[attr])
        return res
