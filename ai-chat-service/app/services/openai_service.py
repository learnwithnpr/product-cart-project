from openai import OpenAI
from app.core.config import settings


client = OpenAI(api_key=settings.OPENAI_API_KEY)


def generate_response(prompt: str) -> str:

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return response.output_text