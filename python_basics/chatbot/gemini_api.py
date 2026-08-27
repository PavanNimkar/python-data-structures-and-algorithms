from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


previous_interaction_id = None


def ask_gemini(message):
    global previous_interaction_id
    response = client.interactions.create(
        model="gemini-3.6-flash",
        input=message,
        previous_interaction_id=previous_interaction_id,
    )

    previous_interaction_id = response.id

    return response.output_text
